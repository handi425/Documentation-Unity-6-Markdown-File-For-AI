[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/profiler-modules-activate.html)
  * [中文](/cn/current/Manual/profiler-modules-activate.html)
  * [日本語](/ja/current/Manual/profiler-modules-activate.html)
  * [한국어](/kr/current/Manual/profiler-modules-activate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/profiler-modules-activate.html)
  * [中文](/cn/current/Manual/profiler-modules-activate.html)
  * [日本語](/ja/current/Manual/profiler-modules-activate.html)
  * [한국어](/kr/current/Manual/profiler-modules-activate.html)

  * [Optimization](analysis.html)
  * [Unity Profiler](Profiler.html)
  * [Collect performance data](profiler-collect-data.html)
  * [Data visualization](profiler-visualizing-data.html)
  * Activating and enabling Profiler modules

[](profiler-modules-introduction.html)

Profiler modules introduction

[](profiler-customizing.html)

Customizing Profiler modules

# Activating and enabling Profiler modules

Profiler modules collect performance data about your application. For
information about **Profiler** A window that helps you to optimize your game.
It shows how much time is spent in the various areas of your game. For
example, it can report the percentage of time spent rendering, animating, or
in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) modules, refer to [Profiler modules
introduction](profiler-modules-introduction.html).

Some Profiler modules have a large data collection overhead, such as the GPU,
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), and audio Profiler module. To prevent
these modules from affecting your application’s performance, you can
deactivate them.

## Activating and deactivating Profiler modules

To activate or deactivate a module:

  1. Open the Profiler window (**Window > Analysis > Profiler**)
  2. Select the **Profiler Modules** dropdown
  3. Enable or disable the modules you want to display

![Profiler windows Profiler Modules dropdown menu](../uploads/Main/profiler-
modules-dropdown.png) Profiler window’s Profiler Modules dropdown menu

Disabling a module removes the module from the window, stops the Profiler from
collecting that module’s data, and lowers the overhead of the Profiler. When
you enable a Profiler module, it starts collecting data, but shows no data for
the period in which it wasn’t active.

**Important:** The [CPU Usage module](ProfilerCPU.html) always collects data
even when it’s not active, because other modules rely on it.

## Reordering Profiler modules

To change the order that the Profiler modules appear in the window, use the
[Profiler Module Editor](profiler-module-editor.html):

  1. Open the Profiler window (**Window > Analysis > Profiler**)
  2. Select the **Profiler Modules** dropdown
  3. Select the cog icon (⚙). The Profiler Module Editor opens in its own window.
  4. Click and drag the handle (≡) next to the module’s name to the desired order.
  5. Select **Save Changes** and close the window

![Profiler Module Editor window](../uploads/Main/profiler-module-editor-
empty.png) Profiler Module Editor window

The Profiler window now displays the new order of Profiler modules.

## Additional resources

  * [Profiler modules introduction](profiler-modules-introduction.html)
  * [Navigating the Profiler window](profiler-window-navigating.html)
  * [Profiler window reference](ProfilerWindow.html)
  * [Profiling your application](profiler-profiling-applications.html)

[](profiler-modules-introduction.html)

Profiler modules introduction

[](profiler-customizing.html)

Customizing Profiler modules

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

