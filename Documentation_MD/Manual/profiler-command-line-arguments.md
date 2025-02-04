[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-command-line-arguments.html)
  * [中文](/cn/current/Manual/profiler-command-line-arguments.html)
  * [日本語](/ja/current/Manual/profiler-command-line-arguments.html)
  * [한국어](/kr/current/Manual/profiler-command-line-arguments.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-command-line-arguments.html)
  * [中文](/cn/current/Manual/profiler-command-line-arguments.html)
  * [日本語](/ja/current/Manual/profiler-command-line-arguments.html)
  * [한국어](/kr/current/Manual/profiler-command-line-arguments.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * Profiler command line arguments

[](profiler-preferences-reference.html)

Profiler Preferences reference

[](profiler-markers.html)

Profiler markers reference

# Profiler command line arguments

Set how the **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) starts from the command line.

If you start your built player or the Unity Editor from the command line (such
as the Command Prompt on Windows, Terminal on macOS, Linux shell, or adb for
Android), you can pass command line arguments to configure some Profiler
settings. For more information about starting Unity from the command line,
refer to [Command line arguments](CommandLineArguments.html).

**Command line argument** | **Description**  
---|---  
`-profiler-enable` | Profile the start-up of a player or the Editor.  
  
When you use this argument with a player, it has the same effect as building
the player with the [Autoconnect Profiler](profiler-build-settings-
reference.html) setting enabled.  
  
When you use this argument with the Editor, it starts collecting and
displaying Profiler information in the Profiler window on start-up of the
Editor.  
`-profiler-log-file <Path/To/Log/File.raw>` | Stream profile data to a .raw file on startup. This argument works for both players and the Editor.  
`-profiler-capture-frame-count <NumberOfFrames>` | Set how many frames to capture in a profile when streaming to a .raw file on start-up. This argument only works on players.  
`-profiler-maxusedmemory` | Set a maximum amount of memory in bytes for the Profiler to use at start up (for example, `-profiler-maxusedmemory 16777216`). By default, `maxUsedMemory` is 16MB for players and 256MB for the Editor.  
`-connection-id` | Set a custom player name set when you launch a player from the command line. You can also set this name in the [Profiler Preferences window](profiler-preferences-reference.html).  
  
## Additional resources

  * [Profiling your application](profiler-profiling-applications.html)
  * [Profiler Preferences reference](profiler-preferences-reference.html)
  * [Profiler Build Profiles settings reference](profiler-build-settings-reference.html)

[](profiler-preferences-reference.html)

Profiler Preferences reference

[](profiler-markers.html)

Profiler markers reference

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

