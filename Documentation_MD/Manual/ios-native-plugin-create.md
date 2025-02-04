[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ios-native-plugin-create.html)
  * [中文](/cn/current/Manual/ios-native-plugin-create.html)
  * [日本語](/ja/current/Manual/ios-native-plugin-create.html)
  * [한국어](/kr/current/Manual/ios-native-plugin-create.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ios-native-plugin-create.html)
  * [中文](/cn/current/Manual/ios-native-plugin-create.html)
  * [日本語](/ja/current/Manual/ios-native-plugin-create.html)
  * [한국어](/kr/current/Manual/ios-native-plugin-create.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * [Native plug-ins for iOS](PluginsForIOS.html)
  * Create a native plug-in for iOS

[](PluginsForIOS.html)

Native plug-ins for iOS

[](ios-native-plugin-use.html)

Use your native plug-in for iOS

# Create a native plug-in for iOS

Create a native **plug-in** A set of code created outside of Unity that
creates functionality in Unity. There are two kinds of plug-ins you can use in
Unity: Managed plug-ins (managed .NET assemblies created with tools like
Visual Studio) and Native plug-ins (platform-specific native code libraries).
[More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) for iOS and import it into your Unity
project.

## Define an extern method

For each native function you want to call, define an extern method in the C#
file as follows:

    
    
    [DllImport ("__Internal")] 
        
    private static extern float FooPluginFunction();
    

## Use C linkage to prevent name mangling

If using C++ (.cpp) or Objective-C++ (.mm) to implement your plug-in, declare
functions with C linkage to avoid issues with name mangling:

    
    
    extern "C" {
      float FooPluginFunction();
    }
    

Plug-ins written in C or Objective-C don’t need this, because these languages
don’t use name mangling.

## Import your native plug-in into your Unity Project

Add your native code source files to the Unity Project’s `Assets` Folder.

## Configure plug-in settings

To configure plug-in settings for iOS:

  1. Select the plug-in and view it in the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)**.

  2. In the **Select platforms for plugin** section, enable **iOS**.
  3. In the **Platform settings** section, set **CPU** to the CPU architecture for your plug-in.
  4. Select **Apply**.

## Additional resources

  * [Use your native plug-in for iOS](ios-native-plugin-use.html)

[](PluginsForIOS.html)

Native plug-ins for iOS

[](ios-native-plugin-use.html)

Use your native plug-in for iOS

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

