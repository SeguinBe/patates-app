/**
 * Created by benoit on 04/07/2016.
 */

var patatesApp = angular.module('patatesApp', ['ui.bootstrap', 'ui.router', "ngAnimate", 'ngMap']);

patatesApp.config(function ($stateProvider, $urlRouterProvider) {

    //
    // For any unmatched url, redirect to /search
    $urlRouterProvider.otherwise("/home");
    //
    // Now set up the states
    $stateProvider
        .state('home', {
            url: "/home",
            templateUrl: "static/partials/home.html"
        })
        .state('about', {
            url: "/about",
            templateUrl: "static/partials/about.html"
        })
        .state('contact', {
            url: "/contact",
            templateUrl: "static/partials/contact.html"
        })
        .state('prices', {
            url: "/prices",
            templateUrl: "static/partials/prices.html"
        })
        .state('culture', {
            url: "/culture",
            templateUrl: "static/partials/culture.html"
        })
        .state('variety', {
            url: "/variety",
            templateUrl: "static/partials/variety.html"
        })
        .state('buy', {
            url: "/buy",
            templateUrl: "static/partials/buy.html"
        })
});

patatesApp.controller('baseController', function($scope, $http) {
    $scope.prices = [];
    /*$http.get("api/prices")
    .then(function(response) {
        $scope.prices = response.data;
    });*/

    $scope.order = {
        email: "",
        firstName: "",
        lastName: "",
        phone: "",
        comments: ""
    };

    $scope.orderMessage = "";

    $scope.clickBuy = function() {
        $http.post("api/buy", $scope.order)
            .then(function(response) {
                $scope.orderMessage = "Email envoyé à : "+$scope.order.email;
            }, function(response) {
                $scope.orderMessage = "La requête a échoué :-(";
            });

    }
});