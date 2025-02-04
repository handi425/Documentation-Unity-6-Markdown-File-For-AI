[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-pinvoke.html)
  * [中文](/cn/current/Manual/uwp-pinvoke.html)
  * [日本語](/ja/current/Manual/uwp-pinvoke.html)
  * [한국어](/kr/current/Manual/uwp-pinvoke.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-pinvoke.html)
  * [中文](/cn/current/Manual/uwp-pinvoke.html)
  * [日本語](/ja/current/Manual/uwp-pinvoke.html)
  * [한국어](/kr/current/Manual/uwp-pinvoke.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)
  * [Use UWP plug-ins with IL2CPP](uwp-il2cpp-plugins.html)
  * Use P/Invoke

[](uwp-native-plugins-author.html)

Author native UWP plug-ins

[](uwp-il2cpp-debugging.html)

Debug UWP applications with IL2CPP

# Use P/Invoke

P/Invoke is a technology that allows you to access structs, callbacks, and
functions in native code from your managed code. The default calling
convention for P/Invoke functions on x86 is `__stdcall`. For more information,
refer to Microsoft documentation on [P/Invoke](https://learn.microsoft.com/en-
us/dotnet/standard/native-interop/pinvoke).

## P/invoke marshaling rules

P/Invoke marshaling rules are the same as those for [.NET
marshaling](https://learn.microsoft.com/en-us/dotnet/standard/native-
interop/type-marshalling). However, Unity doesn’t support the following types:

  * AnsiBStr
  * Currency
  * SAFEARRAY
  * IDispatch
  * TBStr
  * VBByRefStr

## P/invoke limitations

On Universal Windows Platform (UWP), you can’t specify the dynamic-link
library (DLL) name to P/Invoke into specific system libraries. If you try to
P/Invoke into any DLL that exists outside of the project, it will result in a
DllNotFoundException at runtime. Therefore, it’s possible to use the
`__Internal` keyword in place of the DLL name, which will use the C++ linker
to resolve the functions when you build your project, rather than when you
load them at runtime:

    
    
        [DllImport("__Internal")]
        private static extern int CountLettersInString([MarshalAs(UnmanagedType.LPWStr)]string str);
    

If you make an error when you declare a function in your managed code, it will
produce a linker error, rather than an error at runtime. This means that no
dynamic loading needs to take place at runtime and the function is called
directly, which decreases the overhead of a P/Invoke call.

## Additional resources

  * [Microsoft documentation on P/Invoke](https://learn.microsoft.com/en-us/dotnet/standard/native-interop/pinvoke)
  * [Author native UWP plug-ins](uwp-native-plugins-author.html)

[](uwp-native-plugins-author.html)

Author native UWP plug-ins

[](uwp-il2cpp-debugging.html)

Debug UWP applications with IL2CPP

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

