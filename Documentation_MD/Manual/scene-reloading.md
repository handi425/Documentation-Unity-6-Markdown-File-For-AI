[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/scene-reloading.html)
  * [中文](/cn/current/Manual/scene-reloading.html)
  * [日本語](/ja/current/Manual/scene-reloading.html)
  * [한국어](/kr/current/Manual/scene-reloading.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/scene-reloading.html)
  * [中文](/cn/current/Manual/scene-reloading.html)
  * [日本語](/ja/current/Manual/scene-reloading.html)
  * [한국어](/kr/current/Manual/scene-reloading.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Code and scene reload on entering Play mode](code-reloading-editor.html)
  * Enter Play mode with scene reload disabled

[](domain-reloading.html)

Enter Play mode with domain reload disabled

[](configurable-enter-play-mode-details.html)

Details of disabling domain and scene reload

# Enter Play mode with scene reload disabled

Scene reload on entering Play mode is enabled by default. This means that when
you enter Play mode, Unity destroys all existing **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) **GameObjects** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and reloads the scene from disk.
As your project gets more complex, the time between pressing the Play button
and the scene fully loading in the Editor increases.

When you disable scene reloading, the process takes less time. Instead of
reloading the scene from disk, Unity only resets the scene’s modified
contents. Unity still calls the same [event functions](event-functions.html)
(such as `OnEnable`, `OnDisable` and `OnDestroy`) as if the scene were freshly
loaded.

## Effects of disabling scene reload when entering Play mode

When you [disable scene reload](configurable-enter-play-mode.html#configure-
play-mode), the time it takes to start your application in the Editor is no
longer representative of the startup time in the built version. If you want to
debug or profile exactly what happens during your project’s startup, you
should enable scene reloading to more accurately represent the true loading
time and processes that happen in the built version of your application.

Otherwise, disabling scene reload should have minimal effects on your project.
However, because scene reloading is closely connected to domain reload, there
are a few important differences:

  * Unity doesn’t recreate existing objects or call constructors, which means non-serialized fields keep the values assigned to them during Play mode on returning to Edit mode. This applies for fields of all script types, including MonoBehaviours, ScriptableObjects, and your own custom C# types. For detailed information on what is and isn’t serialized in different contexts, refer to [Serialization rules](script-serialization-rules.html). 
    * **Note** : `private` fields are not serialized as part of the regular build pipeline but **are** serialized as part of the Editor’s [hot reloading of scripts](script-serialization-how-unity-uses.html#hot-reload). This is why `private` fields you modify in Play mode might reset to their original values on exiting Play mode even when scene and domain reload on enter Play mode are disabled.
  * Unity converts null `private` and `internal` fields of array and `List` type to an empty array or `List` object during domain reload and they stay non-null for runtime (non-Editor) **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts).

  * Scripts decorated with [`[ExecuteInEditMode]`](../ScriptReference/ExecuteInEditMode.html) or [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) don’t receive `OnDestroy` or `Awake` calls. While in Edit mode, these scripts might modify their own fields or those of other runtime scripts. To mitigate this, you can initialize any affected fields in an `OnEnable` callback with code inside a condition that checks the value of [`EditorApplication.isPlaying`](../ScriptReference/EditorApplication.isPlaying.html). For an example of this and more context on the importance of separating Play mode and Edit mode code, refer to the [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) API description.

For more details on the events skipped with scene reload disabled, refer to
[Details of disabling domain and scene reload](configurable-enter-play-mode-
details.html).

## Additional resources

  * [Configuring code reload on entering Play mode](configurable-enter-play-mode.html)
  * [Enter Play mode with domain reload disabled](domain-reloading.html)
  * [Details of disabling domain and scene reload](configurable-enter-play-mode-details.html)

[](domain-reloading.html)

Enter Play mode with domain reload disabled

[](configurable-enter-play-mode-details.html)

Details of disabling domain and scene reload

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

