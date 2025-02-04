[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-native-plugins-call.html)
  * [中文](/cn/current/Manual/uwp-native-plugins-call.html)
  * [日本語](/ja/current/Manual/uwp-native-plugins-call.html)
  * [한국어](/kr/current/Manual/uwp-native-plugins-call.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-native-plugins-call.html)
  * [中文](/cn/current/Manual/uwp-native-plugins-call.html)
  * [日本語](/ja/current/Manual/uwp-native-plugins-call.html)
  * [한국어](/kr/current/Manual/uwp-native-plugins-call.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)
  * [Use UWP plug-ins with IL2CPP](uwp-il2cpp-plugins.html)
  * Call and implement native UWP plug-ins

[](uwp-managed-plugins.html)

Use managed UWP plug-ins

[](uwp-native-plugins-author.html)

Author native UWP plug-ins

# Call and implement native UWP plug-ins

To call and implement native Universal Windows Platform (UWP) **plug-ins** A
set of code created outside of Unity that creates functionality in Unity.
There are two kinds of plug-ins you can use in Unity: Managed plug-ins
(managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in), you need to know how to create
native plug-ins for Unity. For more information about native plug-ins and
their uses, refer to [Native plug-ins](plug-ins-native.html)A platform-
specific native code library that is created outside of Unity for use in
Unity. Allows you can access features like OS calls and third-party code
libraries that would otherwise not be available to Unity. [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in).

IL2CPP **scripting backend** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) supports the P/Invoke
mechanism for native plug-ins. This means that you can call into native plug-
ins directly from your C# code. To do this, you specify the native function
prototype and then call it.

The following examples show you how to implement a native plug-in and call it
from a C# script.

  1. Create a new .cpp file in your Unity project and insert the following native plug-in code:
    
            extern "C" __declspec(dllexport)
        int __stdcall CountLettersInString(wchar_t* str)
        {
            int length = 0;
            while (*str++ != nullptr)
                length++;
            return length;
        }
    

  2. Create a new C# script and replace its contents with the following code:
    
        [DllImport("MyPlugin.dll")]
        private static extern int CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);
        
        private void Start()
        {
            Debug.Log(CountLettersInString("Hello, native plug-in!"));
        }
    

  3. Add the component to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and enter Play mode. The console will
print 22.

    
        using UnityEngine;
    public class ExamplePlugin : MonoBehaviour
    {
        [DllImport("MyPlugin.dll")]
        private static extern int CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);
        
        private void Start()
        {
            Debug.Log(CountLettersInString("Hello, native plug-in!"));
        }
    }
    

## Additional resources

  * [Native plug-ins](plug-ins-native.html)
  * [Import and configure plug-ins](plug-in-inspector.html)
  * [Use P/invoke](uwp-pinvoke.html)

[](uwp-managed-plugins.html)

Use managed UWP plug-ins

[](uwp-native-plugins-author.html)

Author native UWP plug-ins

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

