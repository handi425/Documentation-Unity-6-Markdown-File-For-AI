[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/memory-allocator-customization.html)
  * [中文](/cn/current/Manual/memory-allocator-customization.html)
  * [日本語](/ja/current/Manual/memory-allocator-customization.html)
  * [한국어](/kr/current/Manual/memory-allocator-customization.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/memory-allocator-customization.html)
  * [中文](/cn/current/Manual/memory-allocator-customization.html)
  * [日本語](/ja/current/Manual/memory-allocator-customization.html)
  * [한국어](/kr/current/Manual/memory-allocator-customization.html)

  * [Optimization](analysis.html)
  * [Memory in Unity](performance-memory.html)
  * [Native memory](performance-native-memory.html)
  * Customizing native memory allocators

[](performance-native-allocators.html)

Native memory allocators

[](performance-native-memory-allocator-reference.html)

Native memory allocators reference

# Customizing native memory allocators

To customize allocator settings you can either edit the configurable values
through the Unity Editor or supply them as command line arguments.

## Using the Editor

  1. Open the **Project Settings** window (**Edit** > **Project Settings**).
  2. Select the **Memory Settings** panel.
  3. Select the lock icon next to the value you want to edit.

![Project Settings > Memory Settings, showing a selection of Player memory
settings](../uploads/Main/memory-native-settings.png) Project Settings >
Memory Settings, showing a selection of Player memory settings

For more information on how the values affect each allocator, refer to [Native
memory allocator examples](performance-native-memory-allocator-examples.html).

## Using command line arguments

You can use [command line arguments](CommandLineArguments.html) to set the
size of each allocator. To find the name of the allocator parameters you want
to change, check the list of allocator settings the Editor and players print
when they start up.

For example, to change the block size of the main heap allocators, use the
following:

`-memorysetup-main-allocator-block-size=<new_value>`

For a full list of command line arguments, refer to [Native memory allocators
reference](performance-native-memory-allocator-reference.html).

## Measuring the performance of changes

To ensure your settings improve performance, [profile your
application](profiler-collect-data.html) before and after making changes. For
more information, refer to the [Profiler overview page](Profiler.html).

You can also use the [Profiler
Analyzer](https://docs.unity3d.com/Packages/com.unity.performance.profile-
analyzer@latest) package to measure changes. The **Profiler** A window that
helps you to optimize your game. It shows how much time is spent in the
various areas of your game. For example, it can report the percentage of time
spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) Analyzer enables you to compare
multiple frames, and two different Profiler captures to each other. Comparing
two captures is useful for highlighting differences in allocator performance
between two different runs with different settings.

You can also check the memory usage reports, which are available in the log
when you close the Player or Editor. To find your log files, follow the
instructions on the [log files page](log-files.html).

## Storing and reading the settings

Unity stores allocator settings in `MemorySettings.asset`, which populates the
`boot.config` file with the modified settings at build time. This means new
settings take effect at every build.

In the Editor, the `boot.config` is in the `ProjectSettings` folder. It gets
updated every time Unity imports or changes `MemorySettings.asset`. New values
for the Editor only take effect on the next Editor startup.

## Additional resources

  * [Native memory allocator examples](performance-native-memory-allocator-examples.html)
  * [Native memory allocators](performance-native-allocators.html)
  * [Native memory allocators reference](performance-native-memory-allocator-reference.html)

[](performance-native-allocators.html)

Native memory allocators

[](performance-native-memory-allocator-reference.html)

Native memory allocators reference

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

