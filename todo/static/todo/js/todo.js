/**
* Main AngularJS Todo Web Application
*/
var app = angular.module('TodoWebApp', ['restangular'])
                 .config(["$provide", function ($provide) {
                    $provide.value("apiRoot", document.getElementById('todoapp')
                                                      .attributes['data-base-url']
                                                      .value);
    }]);;
/**
* Controls tasks
*/
app.controller('TaskCtrl', function ( $scope, Restangular, apiRoot) {
    console.log("Task Controller reporting for duty.");

    var resource = Restangular.all(apiRoot);
    $scope.tasks = [];
    resource.getList().then(function(tasks){
      $scope.tasks = tasks;
    });

    $scope.getTotalTasks = function () {
      return $scope.tasks.length;
    };

    $scope.addTask = function () {
      resource.post({'name': $scope.formTaskText}).then(function(task){
        $scope.tasks.push(task);
      });

      $scope.formTaskText = '';
    };

    $scope.updateTask = function (task) {
      task.patch();
    };

    $scope.clearCompleted = function () {
      _.map($scope.tasks, function(task){
        if(task.is_complete){
          task.remove().then(function(ts) {
            $scope.tasks = _.remove($scope.tasks, function(t) {
              return t.id != task.id;
            });
          });
        }
      });
    };
});


