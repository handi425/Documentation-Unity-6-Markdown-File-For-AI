[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-interacting-browser-unity-to-js.html)
  * [中文](/cn/current/Manual/web-interacting-browser-unity-to-js.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-unity-to-js.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-unity-to-js.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-interacting-browser-unity-to-js.html)
  * [中文](/cn/current/Manual/web-interacting-browser-unity-to-js.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-unity-to-js.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-unity-to-js.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)
  * Call Unity C# script functions from JavaScript

[](web-interacting-browser-js-to-unity.html)

Call JavaScript functions from Unity C# scripts

[](web-interacting-browsers-c-to-unity.html)

Call C/C++/C# functions from Unity C# scripts

# Call Unity C# script functions from JavaScript

You might want to call some Unity code from your JavaScript **plug-in** A set
of code created outside of Unity that creates functionality in Unity. There
are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) or browser code. For example, you
might want a JavaScript **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI) element that triggers a Unity behaviour
and needs access to that method.

The recommended way to send data or notifications to the Unity C# script from
the browser’s JavaScript is to use the `SendMessage` function to call methods
on **GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your Unity project.

## Use the SendMessage helper function

Use `SendMessage` to call a Unity method of the Unity scripting API from
JavaScript code.

There are some restrictions for what sort of methods you can pass. You can
only call methods of a GameObject, not general C# methods attached to other
objects. Also, only use `SendMessage` to call a method if one of the following
is true:

  * The method takes no parameters.
  * The method has one parameter and that parameter is a single string.
  * The method has one parameter and that parameter is a single number.

Methods with more than one parameter or with parameters of other types can’t
be called using `SendMessage`.

## Example SendMessage code

To make the call from a JavaScript plug-in embedded in your project, use the
following code:

    
    
    MyGameInstance.SendMessage(objectName, methodName, value);
    

  * `objectName` is the name of an object in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

  * `methodName` is the name of a method in the script, currently attached to that object.
  * `value` can be a string, a number, or can be empty.

The following code is a further example that shows each of the types of
methods that you can call with different parameters.

    
    
    MyGameInstance.SendMessage('MyGameObject', 'MyFunction');
    MyGameInstance.SendMessage('MyGameObject', 'MyFunction', 5);
    MyGameInstance.SendMessage('MyGameObject', 'MyFunction', 'MyString');
    

To make a call from the global scope of the embedding page, refer to [Call
JavaScript functions from global scope](web-interacting-browser-js-to-
unity.html#global-scope).

## Additional resources

  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)

  * [Set up your JavaScript plug-in](web-interacting-browser-js.html)

  * [Call JavaScript functions from Unity C# scripts](web-interacting-browser-js-to-unity.html)

  * [Call C/C++/C# functions from Unity C# scripts](web-interacting-browsers-c-to-unity.html)

  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](web-interacting-browser-example.html)

[](web-interacting-browser-js-to-unity.html)

Call JavaScript functions from Unity C# scripts

[](web-interacting-browsers-c-to-unity.html)

Call C/C++/C# functions from Unity C# scripts

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

