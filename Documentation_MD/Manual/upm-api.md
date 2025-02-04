[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/upm-api.html)
  * [中文](/cn/current/Manual/upm-api.html)
  * [日本語](/ja/current/Manual/upm-api.html)
  * [한국어](/kr/current/Manual/upm-api.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/upm-api.html)
  * [中文](/cn/current/Manual/upm-api.html)
  * [日本語](/ja/current/Manual/upm-api.html)
  * [한국어](/kr/current/Manual/upm-api.html)

  * [Packages and feature sets](PackagesList.html)
  * [Unity's Package Manager](Packages.html)
  * Scripting API for packages

[](class-PackageManifestImporter.html)

Package Manifest window

[](upm-assets.html)

Accessing package assets

# Scripting API for packages

You can use the Package Manager scripting API to interact with the Package
Manager using C# **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts). For example, you might want to
install a specific package or version depending on the platform of the target
machine.

The system relies heavily on the
[PackageManager.Client](../ScriptReference/PackageManager.Client.html) class,
which you can use to find packages, browse the list of packages, and install
and uninstall packages through scripting.

Another important class is
[PackageManager.PackageInfo](../ScriptReference/PackageManager.PackageInfo.html),
which contains the state of a package, including metadata obtained from the
**package manifest** Each package has a _manifest_ , which provides
information about the package to the Package Manager. The manifest contains
information such as the name of the package, its version, a description for
users, dependencies on other packages (if any), and other details. [More
info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) and the registry. For
example, you can get a [list of
versions](../ScriptReference/PackageManager.VersionsInfo.html) available for
the package, or the [list of any
errors](../ScriptReference/PackageManager.PackageInfo-errors.html) that might
occur while locating or installing the package.

## Adding a package to the project

This example demonstrates how to use the
[Client](../ScriptReference/PackageManager.Client.html) class to install or
add a package to the project.

You can use [Client.Add](../ScriptReference/PackageManager.Client.Add.html) to
add a package. When you call the `Client.Add` method, you can specify just the
package name, or the name with a specific version. For example, using
`Client.Add("com.unity.textmeshpro")` installs (or updates to) the latest
version of the TextMesh Pro package; using
`Client.Add("com.unity.textmeshpro@1.3.0")` installs version 1.3.0 of the
TextMesh Pro package.

The `Client.Add` method returns an
[AddRequest](../ScriptReference/PackageManager.Requests.AddRequest.html)
instance, which you can use to get the status, any errors, or a
[Request](../ScriptReference/PackageManager.Requests.Request_1.Result.html)
response that contains the
[PackageInfo](../ScriptReference/PackageManager.PackageInfo.html) information
for the newly added package.

    
    
    using System;
    using UnityEditor;
    using UnityEditor.PackageManager.Requests;
    using UnityEditor.PackageManager;
    using UnityEngine;
    
    namespace Unity.Editor.Example {
       static class AddPackageExample
       {
           static AddRequest Request;
    
           [MenuItem("Window/Add Package Example")]
           static void Add()
           {
               // Add a package to the project
               Request = Client.Add("com.unity.textmeshpro");
               EditorApplication.update += Progress;
           }
    
           static void Progress()
           {
               if (Request.IsCompleted)
               {
                   if (Request.Status == StatusCode.Success)
                       Debug.Log("Installed: " + Request.Result.packageId);
                   else if (Request.Status >= StatusCode.Failure)
                       Debug.Log(Request.Error.message);
    
                   EditorApplication.update -= Progress;
               }
           }
       }
    }
    

## Browsing the list of packages in a project

This example demonstrates how to use the
[Client](../ScriptReference/PackageManager.Client.html) class to iterate over
the packages in the project.

The [Client.List](../ScriptReference/PackageManager.Client.List.html) method
returns a
[ListRequest](../ScriptReference/PackageManager.Requests.ListRequest.html)
instance, which you can use to get the status of the List operation, any
errors, or a
[Request](../ScriptReference/PackageManager.Requests.Request_1.Result.html)
response that contains the
[PackageCollection](../ScriptReference/PackageManager.PackageCollection.html)
which you can iterate.

    
    
    using System;
    using UnityEditor;
    using UnityEditor.PackageManager.Requests;
    using UnityEditor.PackageManager;
    using UnityEngine;
    
    namespace Unity.Editor.Example {
       static class ListPackageExample
       {
           static ListRequest Request;
    
           [MenuItem("Window/List Package Example")]
           static void List()
           {
               Request = Client.List();    // List packages installed for the project
               EditorApplication.update += Progress;
           }
    
           static void Progress()
           {
               if (Request.IsCompleted)
               {
                   if (Request.Status == StatusCode.Success)
                       foreach (var package in Request.Result)
                           Debug.Log("Package name: " + package.name);
                   else if (Request.Status >= StatusCode.Failure)
                       Debug.Log(Request.Error.message);
    
                   EditorApplication.update -= Progress;
               }
           }
       }
    }
    

## Embedding a package in the project

This example demonstrates how to use the
[Client](../ScriptReference/PackageManager.Client.html) class to [embed](upm-
embed.html) one of the packages already installed in your project. The main
method is the
[Client.Embed](../ScriptReference/PackageManager.Client.Embed.html) method,
which makes a copy of the package and stores it under the `Packages` folder of
your project.

The [Client.Embed](../ScriptReference/PackageManager.Client.Embed.html) method
returns an
[EmbedRequest](../ScriptReference/PackageManager.Requests.EmbedRequest.html)
instance, which you can use to get the status of the Embed operation, any
errors, or a
[Request](../ScriptReference/PackageManager.Requests.Request_1.Result.html)
response that contains the
[PackageInfo](../ScriptReference/PackageManager.PackageInfo.html) information
for the newly **embedded package** An _embedded_ package is a mutable package
that you store under the `Packages` directory at the root of a Unity project.
This differs from most packages which you download from a package server and
are immutable. [More info](upm-concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage).

This example also uses the
[Client.List](../ScriptReference/PackageManager.Client.List.html) method to
access the collection of packages currently installed in your project and
picks out the first one that is neither embedded nor built-in.

The [Client.List](../ScriptReference/PackageManager.Client.List.html) method
returns a
[ListRequest](../ScriptReference/PackageManager.Requests.ListRequest.html)
instance, which you can use to get the status of the List operation, any
errors, or a
[Request](../ScriptReference/PackageManager.Requests.Request_1.Result.html)
response that contains the
[PackageCollection](../ScriptReference/PackageManager.PackageCollection.html)
which you can iterate.

    
    
    using System;
    using System.Collections;
    using System.Collections.Generic;
    using UnityEditor;
    using UnityEditor.PackageManager.Requests;
    using UnityEditor.PackageManager;
    using UnityEngine;
    
    namespace Unity.Editor.Example
    {
        static class EmbedPackageExample
        {
            static String targetPackage;
            static EmbedRequest Request;
            static ListRequest LRequest;
    
            [MenuItem("Window/Embed Package Example")]
            static void GetPackageName()
            {
                // First get the name of an installed package
                LRequest = Client.List();
                EditorApplication.update += LProgress;
            }
    
            static void LProgress()
            {
                if (LRequest.IsCompleted)
                {
                    if (LRequest.Status == StatusCode.Success)
                    {
                        foreach (var package in LRequest.Result)
                        {
                            // Only retrieve packages that are currently installed in the
                            // project (and are neither Built-In nor already Embedded)
                            if (package.isDirectDependency && package.source
                                != PackageSource.BuiltIn && package.source
                                != PackageSource.Embedded)
                            {
                                targetPackage = package.name;
                                break;
                            }
                        }
    
                    }
                    else
                        Debug.Log(LRequest.Error.message);
    
                    EditorApplication.update -= LProgress;
    
                    Embed(targetPackage);
    
                }
            }
    
            static void Embed(string inTarget)
            {
                // Embed a package in the project
                Debug.Log("Embed('" + inTarget + "') called");
                Request = Client.Embed(inTarget);
                EditorApplication.update += Progress;
    
            }
    
            static void Progress()
            {
                if (Request.IsCompleted)
                {
                    if (Request.Status == StatusCode.Success)
                        Debug.Log("Embedded: " + Request.Result.packageId);
                    else if (Request.Status >= StatusCode.Failure)
                        Debug.Log(Request.Error.message);
    
                    EditorApplication.update -= Progress;
                }
            }
        }
    }
    

  

## Package Manager events

Use the [Events](../ScriptReference/PackageManager.Events.html) class to
register an event handler with the Package Manager. The
[Events](../ScriptReference/PackageManager.Events.html) class contains two
events you can subscribe to, which the Package Manager raises at these points:

  * Immediately before the Package Manager changes the list of dependencies ([registeringPackages](../ScriptReference/PackageManager.Events-registeringPackages.html))
  * After the Package Manager imports and compiles the changed list of package dependencies ([registeredPackages](../ScriptReference/PackageManager.Events-registeredPackages.html))

The following examples demonstrate how to use both of these events.

### Example of using the registeringPackages event

    
    
    using UnityEditor.PackageManager;
    using UnityEngine;
    
    namespace Unity.Editor.Example
    {
        public class EventSubscribingExample_RegisteringPackages
        {
            public EventSubscribingExample_RegisteringPackages()
            {
                // Subscribe to the event using the addition assignment operator (+=).
                // This executes the code in the handler whenever the event is fired.
                Events.registeringPackages += RegisteringPackagesEventHandler;
            }
    
            // The method is expected to receive a PackageRegistrationEventArgs event argument.
            void RegisteringPackagesEventHandler(PackageRegistrationEventArgs packageRegistrationEventArgs)
            {
                Debug.Log("The list of registered packages is about to change!");
    
               foreach (var addedPackage in packageRegistrationEventArgs.added)
                {
                    Debug.Log($"Adding {addedPackage.displayName}");
                }
    
                foreach (var removedPackage in packageRegistrationEventArgs.removed)
                {
                    Debug.Log($"Removing {removedPackage.displayName}");
                }
    
                // The changedFrom and changedTo collections contain the packages that are about to be updated.
                // Both collections are guaranteed to be the same size with indices matching the same package name.
                for (int i = 0; i <= packageRegistrationEventArgs.changedFrom.Count; i++)
                {
                    var oldPackage = packageRegistrationEventArgs.changedFrom[i];
                    var newPackage = packageRegistrationEventArgs.changedTo[i];
    
                    Debug.Log($"Changing ${oldPackage.displayName} version from ${oldPackage.version} to ${newPackage.version}");
                }
            }
        }
    }
    

### Example of using the registeredPackages event

    
    
    using UnityEditor;
    using UnityEditor.PackageManager;
    using UnityEngine;
    
    namespace Unity.Editor.Example
    {
        public class EventSubscribingExample_RegisteredPackages
        {
            // You must use '[InitializeOnLoadMethod]' or '[InitializeOnLoad]' to subscribe to this event.
            [InitializeOnLoadMethod]
            static void SubscribeToEvent()
            {
                // This causes the method to be invoked after the Editor registers the new list of packages.
                Events.registeredPackages += RegisteredPackagesEventHandler;
            }
    
            static void RegisteredPackagesEventHandler(PackageRegistrationEventArgs packageRegistrationEventArgs)
            {
                // Code executed here can safely assume that the Editor has finished compiling the new list of packages
                Debug.Log("The list of registered packages has changed!");
            }
        }
    }
    

[](class-PackageManifestImporter.html)

Package Manifest window

[](upm-assets.html)

Accessing package assets

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

