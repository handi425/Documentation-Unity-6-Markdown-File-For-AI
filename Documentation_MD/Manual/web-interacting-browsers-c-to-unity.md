[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-interacting-browsers-c-to-unity.html)
  * [中文](/cn/current/Manual/web-interacting-browsers-c-to-unity.html)
  * [日本語](/ja/current/Manual/web-interacting-browsers-c-to-unity.html)
  * [한국어](/kr/current/Manual/web-interacting-browsers-c-to-unity.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-interacting-browsers-c-to-unity.html)
  * [中文](/cn/current/Manual/web-interacting-browsers-c-to-unity.html)
  * [日本語](/ja/current/Manual/web-interacting-browsers-c-to-unity.html)
  * [한국어](/kr/current/Manual/web-interacting-browsers-c-to-unity.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)
  * Call C/C++/C# functions from Unity C# scripts

[](web-interacting-browser-unity-to-js.html)

Call Unity C# script functions from JavaScript

[](web-interacting-browsers-library.html)

Compile a static library as a Unity plug-in

# Call C/C++/C# functions from Unity C# scripts

You can call functions from your C, C++, or C# **plug-ins** A set of code
created outside of Unity that creates functionality in Unity. There are two
kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET
assemblies created with tools like Visual Studio) and Native plug-ins
(platform-specific native code libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) in your Unity projects.

Unity uses Emscripten to compile your sources into WebAssembly from C/C++/C#
code, so you can write plug-ins in C/C++/C# code and call these functions from
your Unity C# **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

To call functions from your JavaScript plug-ins instead, refer to [Call
JavaScript functions from Unity C# scripts](web-interacting-browser-js-to-
unity.html).

## Import your C/C++/C# plug-in into your Unity project

To allow your Unity project to call functions from your C/C++/C# plug-in code,
you need to import your plug-in into your Unity project.

Place your JavaScript plug-in files in any folder, such as `Assets/JSPlugins`.

## Example C++ code that you can use in Unity

If you use C++ (.cpp) to implement the plug-in, you must declare the functions
with C linkage (`extern “C”`) to avoid name mangling issues. The following
code is an example C++ plug-in with simple functions that you can call in your
Unity project.

    
    
    #include <stdio.h>
    
    extern "C" void Hello ()
    {
        printf("Hello, world!\n");
    }
    
    extern "C" int AddNumbers (int x, int y)
    {
        return x + y;
    }
    

**Note** : Unity uses the Emscripten version 2.0.19 toolchain.

Use the following Unity C# code in your Unity project to call the C++
functions.

    
    
    using UnityEngine;
    using System.Runtime.InteropServices;
    
    public class NewBehaviourScript : MonoBehaviour {
    
        [DllImport("__Internal")]
        private static extern void Hello();
    
        [DllImport("__Internal")]
        private static extern int AddNumbers(int x, int y);
    
        void Start() {
            Hello();
            
            int result = AddNumbers(5, 7);
            Debug.Log(result);  
        }
    }
    

## Additional resources

  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)

  * [Set up your JavaScript plug-in](web-interacting-browser-js.html)

  * [Call JavaScript functions from Unity C# scripts](web-interacting-browser-js-to-unity.html)

  * [Call Unity C# script functions from JavaScript](web-interacting-browser-unity-to-js.html)

  * [Create callbacks between Unity C#, JavaScript, and C/C++/C# code](web-interacting-browser-example.html)

[](web-interacting-browser-unity-to-js.html)

Call Unity C# script functions from JavaScript

[](web-interacting-browsers-library.html)

Compile a static library as a Unity plug-in

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

