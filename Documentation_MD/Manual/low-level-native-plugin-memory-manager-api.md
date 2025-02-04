[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/low-level-native-plugin-memory-manager-api.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-memory-manager-api.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-memory-manager-api.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-memory-manager-api.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/low-level-native-plugin-memory-manager-api.html)
  * [中文](/cn/current/Manual/low-level-native-plugin-memory-manager-api.html)
  * [日本語](/ja/current/Manual/low-level-native-plugin-memory-manager-api.html)
  * [한국어](/kr/current/Manual/low-level-native-plugin-memory-manager-api.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Integrating third-party code libraries (plug-ins)](plug-ins.html)
  * [Low-level native plug-in interface](native-plugin-interface.html)
  * Memory Manager API for low-level native plug-ins

[](low-level-native-plugin-shader-compiler-access.html)

Low-level native plug-in Shader compiler access

[](low-level-native-plugin-memory-manager-api-reference.html)

IUnityMemoryManager API reference

# Memory Manager API for low-level native plug-ins

The `IUnityMemoryManager` memory manager API is a C++ interface that allows
you to use Unity’s memory management and memory profiling in native **plug-
ins** A set of code created outside of Unity that creates functionality in
Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins
(managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in).

This API enables you to:

  * Access Unity’s memory manager through a memory allocator.
  * Track your plug-in’s memory use through Unity’s Memory **Profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) package.

These features make it easier to manage and profile your plug-in’s memory
allocations when compared to the equivalent C++ memory management methods.

The plug-in API is provided by the IUnityMemoryManager interface, which is
declared in the `IUnityMemoryManager.h` header. The full reference for the API
is available in this file. To find the header file:

  * On Windows, Unity stores the header in the `<UnityInstallPath>\Editor\Data\PluginAPI` folder of your Unity installation.
  * On macOS, right-click on the Unity application, and select Show Package Contents. The header is in `Contents\PluginAPI`.

You should be familiar with the following concepts to use this API
effectively:

  * [C++ Pointers](https://learn.microsoft.com/en-us/cpp/cpp/pointers-cpp?view=msvc-170)
  * [Memory in Unity](performance-memory-overview.html)
  * [The Memory Profiler package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
  * [Memory allocator customization](memory-allocator-customization.html)
  * [Predefined macros](https://learn.microsoft.com/en-us/cpp/preprocessor/predefined-macros?view=msvc-170)

## Track memory use in Unity

To track your plug-in’s memory usage, use the [Memory Profiler
package](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest) to
take a snapshot, then open the snapshot in the [All Of Memory
tab](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/index.html?subfolder=/manual/all-
memory-tab.html). When you use the `IUnityMemoryManager` to allocate memory,
the Memory Profiler displays the plug-in’s memory allocations under the area
and object name you assigned when you created each allocator.

The below screenshot shows the Memory Profiler package window displaying
memory used by a native plug-in with memory allocated with the
`IUnityMemoryManager` API. In this example, the method **CreateAllocator** was
called, with “MyNativePlugin” as the areaName parameter, and
“MyPluginAllocator” as the objectName parameter. For more information, refer
to [IUnityMemoryManager API reference](low-level-native-plugin-memory-manager-
api-reference.html).

![The Memory Profiler package window displaying the memory used by a user-
defined allocator named Plugin Backend Allocator.](../uploads/Main/native-
plugin-memory-snapshot.png) The Memory Profiler package window displaying the
memory used by a user-defined allocator named Plugin Backend Allocator.

For more information, see
[Snapshots](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest/index.html?subfolder=/manual/snapshots.html).

## Memory management limitations

This API enables you to use Unity’s memory management system when you develop
native plug-ins. This has major benefits as described above, but there are
still limitations. Unity’s memory management system:

  * Isn’t automatically managed; you need to allocate and deallocate the memory yourself.
  * Isn’t tracked and cleaned up by a garbage collector.

Since memory in native C++ isn’t managed, you need to keep track of any memory
requirements your application has. This includes choosing the correct amount
of memory to allocate and making sure you deallocate it when it’s no longer
needed.

The `IUnityMemoryManager` API impacts performance because each allocation
requires a virtual call. To minimize this performance impact, use the API to
allocate larger blocks of memory less frequently. To handle smaller and more
frequent allocations, use this API to allocate a single larger block, then
write your own code to manage the memory within this block. Don’t use this API
for frequent small allocations.

## Additional resources

  * [Native Plug-in interface](native-plugin-interface.html) \- Explains the base interface that this API inherits from.
  * [Native plug-ins](plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Nativeplug-in) \- Explains what a native plug-
in is.

  * [Memory allocator customization](memory-allocator-customization.html) \- Explains how to customize Unity’s internal memory allocators.

[](low-level-native-plugin-shader-compiler-access.html)

Low-level native plug-in Shader compiler access

[](low-level-native-plugin-memory-manager-api-reference.html)

IUnityMemoryManager API reference

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

