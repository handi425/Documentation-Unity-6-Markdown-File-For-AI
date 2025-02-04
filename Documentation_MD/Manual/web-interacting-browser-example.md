[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-interacting-browser-example.html)
  * [中文](/cn/current/Manual/web-interacting-browser-example.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-example.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-example.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-interacting-browser-example.html)
  * [中文](/cn/current/Manual/web-interacting-browser-example.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-example.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-example.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)
  * Create callbacks between Unity C#, JavaScript, and C/C++/C# code

[](web-interacting-browsers-library.html)

Compile a static library as a Unity plug-in

[](web-js-interface.html)

JavaScript interface in Unity Web builds

# Create callbacks between Unity C#, JavaScript, and C/C++/C# code

Callbacks are an important part of web development because they let your Unity
project communicate better with your JavaScript browser, JavaScript **plug-
in** A set of code created outside of Unity that creates functionality in
Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins
(managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in), and C/C++/C# plug-ins. You might
want to call functions from your C/C++/C# or JavaScript code in your Unity C#
code, and callbacks are an effective way to do this.

## Use the makeDynCall function to make callbacks

Use `makeDynCall` to call C, C++, or C# callbacks from JavaScript code. For
example, the following JavaScript code calls the function “callback”:

    
    
    {{{ makeDynCall('vii', 'callback') }}}(1, 2)
    

  * `'vii'` is the signature of the parameters. For example, the callback function is a `void` type (v), and the `(1,2)` are both integers (ii).
  * `'callback'` is the name of the callback function.
  * `(1, 2)` are the arguements to pass into the function.

The following code is another example of code that does a callback with the
function “onresponse” and passes in a float (f) and multiple integer type
values:

    
    
    {{{ makeDynCall('vfii', 'onresponse') }}}(2.8, arg, 0);
    

## Use callbacks in your scripts

The following **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) show an example of how to use
callback functions to communicate between JavaScript, C++, and C# code.

### Javascript plug-in code

The following code is an example of a `.jslib` file that schedules a timeout
and invokes a callback.

    
    
    mergeInto(LibraryManager.library, {
        JsSetTimeout: function (message, timeout, callback) {
            // Create copy of message because it might be deleted before callback is run
            var stringMessage = UTF8ToString(message);
            var buffer = stringToNewUTF8(stringMessage);
            setTimeout(function () {
                {{{ makeDynCall('vi', 'callback') }}} (buffer);
                _free(buffer);
            }, timeout);
        }
    });
    

### C++ plug-in code

The following code is an example of a C++ file that: * calls the external
JavaScript function (`JsSetTimeout`) * contains the callback function the
JavaScript calls when a timeout happens.

    
    
    // CallbackExample.cpp
    #include <stdio.h>
    
    typedef void (*OnTimeOutCallback)(char* message);
    
    extern "C"
    {
        void JsSetTimeout(char* message, int timeout, OnTimeOutCallback callback);
    }
    
    void CCallback(char* message)
    {
        printf("C callback received \"%s\"\n", message);
    }
    
    extern "C" void SetCTimeout()
    {
        JsSetTimeout("Hello World", 1000, CCallback);
    }
    

### Unity C# code

The following code is an example of C# Unity code that receives the messages
from the C++ and JavaScript callbacks.

    
    
    using AOT;
    using System;
    using System.Text;
    using System.Runtime.InteropServices;
    using UnityEngine;
    
    public class CallbackExample : MonoBehaviour
    {
        void Awake()
        {
            SetCSharpTimeout();
            SetCTimeout();
        }
    
        void SetCSharpTimeout()
        {
            JsSetTimeout("Hello World", 500, CSSharpCallback);
        }
    
        [DllImport("__Internal")]
        public static extern void SetCTimeout();    
        
        [DllImport("__Internal")]
        public static extern void JsSetTimeout(string message, int timeout, Action<string> action);
    
        [MonoPInvokeCallback(typeof(Action<string>))]
        public static void CSSharpCallback(string message)
        {
           Debug.Log($"C# callback received \"{message}\"");
        }
    }
    

## Additional resources

  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)

  * [Set up your JavaScript plug-in](web-interacting-browser-js.html)

  * [Call JavaScript functions from Unity C# scripts](web-interacting-browser-js-to-unity.html)

  * [Call Unity C# script functions from JavaScript](web-interacting-browser-unity-to-js.html)

  * [Call C/C++/C# functions from Unity C# scripts](web-interacting-browsers-c-to-unity.html)

  * [Replace deprecated browser interaction code](web-interacting-browser-deprecated.html)

[](web-interacting-browsers-library.html)

Compile a static library as a Unity plug-in

[](web-js-interface.html)

JavaScript interface in Unity Web builds

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

