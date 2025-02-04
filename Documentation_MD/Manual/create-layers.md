[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/create-layers.html)
  * [中文](/cn/current/Manual/create-layers.html)
  * [日本語](/ja/current/Manual/create-layers.html)
  * [한국어](/kr/current/Manual/create-layers.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/create-layers.html)
  * [中文](/cn/current/Manual/create-layers.html)
  * [日本語](/ja/current/Manual/create-layers.html)
  * [한국어](/kr/current/Manual/create-layers.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with scenes](working-with-scenes.html)
  * [Layers](Layers.html)
  * Create functional layers in Unity

[](use-layers.html)

Uses of layers in Unity

[](LayerBasedCollision.html)

Layer-based collision detection

# Create functional layers in Unity

Layers can help to organize the **GameObjects** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). If you create a layer and assign
GameObjects to it, you can edit how your GameObjects interact with other
GameObjects, dependent on the layer.

## Add a new layer

There are two ways you can create a new layer:

  * Select the [Tags and Layers window](class-TagManager.html) (main menu: **Edit** > **Project Settings** > **Tags and Layers** > **Layers**).
  * Select a GameObject, select the **Layer** dropdown in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window, and select **Add Layer**
from the menu.

To remember the intended function for a layer, give it a descriptive name.

**Warning** : Layer 31 is used internally by the Editor’s Preview window
mechanics. To prevent clashes, do not use this layer.

### Built-in layers

When you open the layer menu, you can see that some layers are already named.
Except for Default and Ignore Raycast, Unity no longer uses these built-in
layers for many dedicated purposes; they exist mainly for backward
compatibility:

**Layer number** | **Layer name** | **Description**  
---|---|---  
**0** | Default | The default layer for all scene elements.  
**1** | TransparentFX | Unity uses this layer in the [flare system](class-Flare.html).  
**2** | Ignore Raycast | Physics ray cast APIs ignore this layer by default.  
**4** | Water | Unity’s [Standard Assets for Unity 2018.4](https://assetstore.unity.com/packages/essentials/asset-packs/standard-assets-for-unity-2018-4-32351) use this layer.  
**5** | **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) | The [Unity UI](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html) uses this as the default layer for UI elements.  
  
You can still use these layers, but you can’t rename or delete them.

## Add GameObjects to a layer

To assign a GameObject to a layer, select the GameObject, go to the Inspector
window and select the dropdown next to **Layer**. This menu shows the layers
that have names so you can select which one works best for your GameObject.

You can only assign each GameObject to one layer, but you can add multiple
GameObjects to one layer.

## Additional resources

  * [Essential Unity concepts](https://learn.unity.com/tutorial/essential-unity-concepts#5c7f8528edbc2a002053b6c8)
  * [Tags and layers](class-TagManager.html)

[](use-layers.html)

Uses of layers in Unity

[](LayerBasedCollision.html)

Layer-based collision detection

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

