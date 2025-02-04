[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/uwp-debug-generated-cpp.html)
  * [中文](/cn/current/Manual/uwp-debug-generated-cpp.html)
  * [日本語](/ja/current/Manual/uwp-debug-generated-cpp.html)
  * [한국어](/kr/current/Manual/uwp-debug-generated-cpp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/uwp-debug-generated-cpp.html)
  * [中文](/cn/current/Manual/uwp-debug-generated-cpp.html)
  * [日本語](/ja/current/Manual/uwp-debug-generated-cpp.html)
  * [한국어](/kr/current/Manual/uwp-debug-generated-cpp.html)

  * [Platform development ](PlatformSpecific.html)
  * [Universal Windows Platform](WindowsStore.html)
  * [Develop for Universal Windows Platform](uwp-developing.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)
  * [Debug UWP applications with IL2CPP](uwp-il2cpp-debugging.html)
  * Debug generated C++ code

[](uwp-debug-c-sharp.html)

Debug C# code

[](windowsstore-scripts.html)

WinRT API in C# scripts for UWP

# Debug generated C++ code

You can debug generated C++ code for your Universal Windows Platform (UWP)
application using Visual Studio.

## Understand class and method naming in generated C++ code

### IL2CPP classes

IL2CPP classes follow the format of `<ClassName>_t#number`, where:

  * `<ClassName>` is the class name
  * The optional `#number` is a unique type number

Example **IL2CPP** A Unity-developed scripting back-end which you can use as
an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) classes:

  * `String_t` \- [String class](https://learn.microsoft.com/en-us/dotnet/api/system.string)
  * `Object_t` \- [Object class](https://learn.microsoft.com/en-us/dotnet/api/system.object)
  * `Type_t` \- [Type class](https://learn.microsoft.com/en-us/dotnet/api/system.type)
  * `StringBuilder_t26` \- [StringBuilder class](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder)

### IL2CPP methods

IL2CPP methods follow the format of `<ClassName>_<MethodName>_m#number`,
where:

  * `<ClassName>` is the class name of the method’s declaring type
  * `<MethodName>` is the method name
  * `#number` is a unique method number

Example IL2CPP methods:

  * `ConfigurationSection_DoDeserializeSection_m1275` \- [DeserializationSection method of the ConfigurationSection class](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationsection.deserializesection)
  * `String_Format_m4102` \- [Format method of the String class](https://learn.microsoft.com/en-us/dotnet/api/system.string.format)
  * `Mathf_Sqrt_m289` \- [Sqrt method of the Mathf class](https://learn.microsoft.com/en-us/dotnet/api/system.mathf.sqrt)

### IL2CPP static field structures

Static fields structures follow the format of
`<ClassName>_t#number_StaticFields`, where the first part of the structure
name is the same as the declaring type.

Example static fields structures:

  * `StringBuilder_t26_StaticFields`
  * `Thing_t24_StaticFields`

### C++ comments

Preceding each class or method definition, C++ automatically generates a
comment stating the full class or method name.

Example C++ comment:

    
    
        // System.Text.StringBuilder
        struct StringBuilder_t26  : public Object_t
        {
            // System.Int32 System.Text.StringBuilder::_length
            int32_t length_1;
            // System.Int32 System.Text.StringBuilder::_maxCapacity
            int32_t maxCapacity_2;
        };
    

## Observe variable values

You can debug your generated C++ code by observing the values of your
variables [using the Visual Studio debugger](https://learn.microsoft.com/en-
us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-
unity?pivots=windows#unity-debugging).

You can [set breakpoints in Visual Studio](managed-code-
debugging.html#BreakpointsVS) where you want the debugger to stop so you can
observe your variables. Visual Studio allows you to observe your variable
values by either mousing over the variable or [using a Watch
window](https://learn.microsoft.com/en-us/visualstudio/debugger/watch-and-
quickwatch-windows?).

## Observe a static field

In IL2CPP, Unity stores static fields in an Il2CppClass instance. To observe
the values of the static field, you need to:

  1. Find the [pointer](https://learn.microsoft.com/en-us/cpp/cpp/pointers-cpp) to the Il2CppClass structure of that type in your code.   
**Note:** These pointers are in scope of the methods that use them, but after
observing it once, it will remain at the same memory address during the
application run.

  2. Retrieve the value of the `static_fields` field from that pointer. This is a pointer to a memory block containing static fields for that particular type.
  3. Cast the value to the corresponding static field structure.
  4. Observe the value in [the Visual Studio debugger](https://learn.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-unity?pivots=windows#unity-debugging).

## Investigate exceptions

IL2CPP uses native C++ exceptions to implement .NET exceptions.

To investigate the exceptions in your code, you can:

  * Inspect the exception objects in the [watch window](https://learn.microsoft.com/en-us/visualstudio/debugger/watch-and-quickwatch-windows?)
  * [Enable the debugger to break](https://learn.microsoft.com/en-us/visualstudio/debugger/managing-exceptions-with-the-debugger) on C++ exceptions

## Additional resources

  * [Microsoft documentation on how to Debug C++ code using Visual Studio](https://learn.microsoft.com/en-us/visualstudio/debugger/getting-started-with-the-debugger-cpp?)
  * [Microsoft documentation on Unity debugging with Visual Studio](https://learn.microsoft.com/en-us/visualstudio/gamedev/unity/get-started/using-visual-studio-tools-for-unity?pivots=windows#unity-debugging)
  * [IL2CPP overview](./scripting-backends-il2cpp.html)
  * [IL2CPP scripting backend for UWP](uwp-il2cpp-scripting.html)

[](uwp-debug-c-sharp.html)

Debug C# code

[](windowsstore-scripts.html)

WinRT API in C# scripts for UWP

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

