[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-interacting-browser-deprecated.html)
  * [中文](/cn/current/Manual/web-interacting-browser-deprecated.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-deprecated.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-deprecated.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-interacting-browser-deprecated.html)
  * [中文](/cn/current/Manual/web-interacting-browser-deprecated.html)
  * [日本語](/ja/current/Manual/web-interacting-browser-deprecated.html)
  * [한국어](/kr/current/Manual/web-interacting-browser-deprecated.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Web development](webgl-develop.html)
  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)
  * Replace deprecated browser interaction code

[](web-js-interface.html)

JavaScript interface in Unity Web builds

[](webgl-native-plugins-with-emscripten.html)

Web native plug-ins for Emscripten

# Replace deprecated browser interaction code

Some code involved with web browser script interactions is deprecated and has
been replaced with alternative code.

If your code contains any of the deprecated code, you need to update the code
with the replacement code to prevent unexpected behavior or broken code.

## Deprecated code quick reference

The following code is deprecated and you need to replace it with the
replacement code.

Deprecated code | Replacement code  
---|---  
dynCall() | `makeDynCall()`  
Pointer_stringify() | `UTF8ToString()`  
unity.Instance() | `CreateUnityInstance()`  
gameInstance | `unityInstance`  
  
## Change dynCall to makeDynCall

The `dynCall` function is deprecated. If you have any code that uses
`dynCall`, replace it with `makeDynCall`. Make this change whether you have
`WebAssembly.Table` enabled or not.

For example, change:

    
    
    dynCall('vii', callback, [1, 2])
    

to:

    
    
    {{{ makeDynCall('vii', 'callback') }}}(1, 2)
    

## Change Pointer_stringify() to UTF8ToString

The `Pointer_stringify()` function is deprecated. If your code contains calls
to `Pointer_stringify()`, replace the calls with `UTF8ToString()`.

For example, change:

    
    
    var stringMessage = Pointer_stringify(message);
    

to:

    
    
    var stringMessage = UTF8ToString(message);
    

## Change unity.Instance to CreateUnityInstance

`unity.Instance` is deprecated. If your code uses `unity.Instance`, use
`CreateUnityInstance` instead.

For example, change:

    
    
    var MyGameInstance = null;
      script.onload = () => {
        unity.Instance(canvas, config, (progress) => { /*...*/ }).then((unityInstance) => {
    

to:

    
    
    var MyGameInstance = null;
      script.onload = () => {
        createUnityInstance(canvas, config, (progress) => { /*...*/ }).then((unityInstance) => {
    

## Change gameInstance to unityInstance

The `gameInstance` property is deprecated. If your code uses `gameInstance`,
use `unityInstance` instead.

For example, change:

    
    
    MyGameInstance = gameInstance;
    

to:

    
    
    MyGameInstance = unityInstance;
    

## Additional resources

  * [Interaction with browser scripting](webgl-interactingwithbrowserscripting.html)

  * [Set up your JavaScript plug-in](web-interacting-browser-js.html)

  * [Call JavaScript functions from Unity C# scripts](web-interacting-browser-js-to-unity.html)

  * [Call Unity C# script functions from JavaScript](web-interacting-browser-unity-to-js.html)

  * [Call C/C++/C# functions from Unity C# scripts](web-interacting-browsers-c-to-unity.html)

[](web-js-interface.html)

JavaScript interface in Unity Web builds

[](webgl-native-plugins-with-emscripten.html)

Web native plug-ins for Emscripten

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

