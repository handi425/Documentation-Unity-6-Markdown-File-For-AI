[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/running-editor-code-on-launch.html)
  * [中文](/cn/current/Manual/running-editor-code-on-launch.html)
  * [日本語](/ja/current/Manual/running-editor-code-on-launch.html)
  * [한국어](/kr/current/Manual/running-editor-code-on-launch.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/running-editor-code-on-launch.html)
  * [中文](/cn/current/Manual/running-editor-code-on-launch.html)
  * [日本語](/ja/current/Manual/running-editor-code-on-launch.html)
  * [한국어](/kr/current/Manual/running-editor-code-on-launch.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * Running project code on Editor launch

[](configurable-enter-play-mode-details.html)

Details of disabling domain and scene reload

[](script-serialization.html)

Script serialization

# Running project code on Editor launch

Sometimes it can be useful to make parts of your Edit mode project code run
immediately when the Unity Editor launches without requiring any user action.
You can do this by applying the
[InitializeOnLoad](../ScriptReference/InitializeOnLoadAttribute.html)
attribute to a class which has a static constructor. A static constructor is a
function with the same name as the class, declared `static` and without a
return type or parameters. For more information, refer to [Static
constructors](https://learn.microsoft.com/en-us/dotnet/csharp/programming-
guide/classes-and-structs/static-constructors) in the Microsoft C#
documentation.

    
    
    using UnityEngine;
    using UnityEditor;
    
    [InitializeOnLoad]
    public class Startup {
        static Startup()
        {
            Debug.Log("Up and running");
        }
    }
    
    

A static constructor is always guaranteed to be called before any static
function or instance of the class is used, but the `InitializeOnLoad`
attribute ensures it’s called when the Editor launches. Static constructors
with this attribute are called when **scripts** A piece of code that allows
you to create your own Components, trigger game events, modify Component
properties over time and respond to user input in any way you like. [More
info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the project are recompiled, also
known as a [domain reload](domain-reloading.html). This happens when:

  * Unity first loads your project.
  * Unity detects modifications to scripts, if **Auto Refresh** is enabled in the Asset Pipeline section of the [Preferences window](Preferences.html).
  * Entering Play Mode, if Domain Reload is enabled in your [Play Mode configuration](configurable-enter-play-mode.html).

An example use of the initialize on load functionality is setting up a regular
callback which could be thought of as a sort of “frame update” for the Editor
application. The
[EditorApplication](../ScriptReference/EditorApplication.html) class has a
delegate called [update](../ScriptReference/EditorApplication-update.html)
which is called many times per second while the Editor is running. The
following code example defines a small custom class decorated with
`[InitializeOnLoad]` and assigns a member method to the
`EditorApplication.update` delegate so that it runs and begins printing
`Updating` to the console on Editor launch:

    
    
    using UnityEditor;
    using UnityEngine;
    
    // InitializeOnLoad ensures this code runs on Editor launch
    [InitializeOnLoad]
    class MyClass
    {
        // Define a static constructor in which we assign the custom Update method to the delegate
        static MyClass ()
        {
            EditorApplication.update += Update;
        }
    
        // Define a method with the required signature that performs work we want to do on launch
        static void Update ()
        {
            Debug.Log("Updating");
        }
    }
    
    

## Additional resources

  * [Configurable Enter Play Mode](configurable-enter-play-mode.html)
  * [Domain Reloading](domain-reloading.html)
  * [InitializeOnLoadAttribute](../ScriptReference/InitializeOnLoadAttribute.html)

[](configurable-enter-play-mode-details.html)

Details of disabling domain and scene reload

[](script-serialization.html)

Script serialization

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

