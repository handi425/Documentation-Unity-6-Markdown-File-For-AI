[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/create-lens-flare.html)
  * [中文](/cn/current/Manual/create-lens-flare.html)
  * [日本語](/ja/current/Manual/create-lens-flare.html)
  * [한국어](/kr/current/Manual/create-lens-flare.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/create-lens-flare.html)
  * [中文](/cn/current/Manual/create-lens-flare.html)
  * [日本語](/ja/current/Manual/create-lens-flare.html)
  * [한국어](/kr/current/Manual/create-lens-flare.html)

  * [Visual effects](visual-effects.html)
  * [Lens flares](visual-effects-lens-flares.html)
  * [Lens flares in the Built-In Render Pipeline](lens-flare-birp.html)
  * Create a lens flare

[](lens-flare-birp.html)

Lens flares in the Built-In Render Pipeline

[](configuring-flare-elements.html)

Configuring Flare elements

# Create a lens flare

Create a flare and apply it to a lens flare component, then configure it to be
visible by cameras.

**Note:** This workflow is compatible only with the Built-in **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). For similar functionality in
other render pipelines, see [Lens flares and halos](visual-effects-lens-
flares.html).

## Apply a Flare asset

  1. Assign the Flare asset to a [Light component](class-Light.html) or a [Lens flare component](class-LensFlare.html). 
     * If you assign it to the **Flare** property of a [Light component](class-Light.html), Unity automatically tracks the position and direction of the Light and uses those values to configure the appearance of the lens flare.
     * If you assign it to the **Flare** property of a [Lens flare component](class-LensFlare.html), you can use the Lens Flare component to configure additional values for more precise control.
  2. If you want a [Camera](class-Camera.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) to see lens flares, attach a [Flare
Layer](class-FlareLayer.html) component to the Camera’s GameObject.

  3. To see the lens flare effect in the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView), enable the Effect toggle in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View **toolbar** A row of buttons and
basic controls at the top of the Unity Editor that allows you to interact with
the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) and, in the drop-down, enable
**Flares**.

## Create a lens flare with the Lens Flare component

  1. Create a new **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) (menu bar: **GameObject > Create
Empty**).

  2. In the Inspector, click **Add Component > Effects > Lens Flare**.
  3. Assign a [Flare Asset](class-Flare.html) to the **Flare** property.
  4. If you want a [Camera](class-Camera.html) to see lens flares, attach a [Flare Layer](class-FlareLayer.html) component to the Camera’s GameObject.
  5. To see the lens flare effect in the **Scene View** , enable the Effect toggle in the Scene View toolbar and, in the drop-down, enable **Flares**.

![Enable the Effect toggle to view lens flares in the Scene
view](../uploads/Main/LensFlare-FXButton.png) Enable the Effect toggle to view
lens flares in the Scene view

## Make a lens flare visible to a camera

In the Built-in Render Pipeline, if you want a [Camera](class-Camera.html) to
see [lens flares](class-Flare.html)A component that simulates the effect of
lights refracting inside a camera lens. Use a Lens Flare to represent very
bright lights or add atmosphere to your scene. [More info](class-
LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare), you must attach a [Flare
Layer](class-FlareLayer.html) component to the Camera’s GameObject.

[](lens-flare-birp.html)

Lens flares in the Built-In Render Pipeline

[](configuring-flare-elements.html)

Configuring Flare elements

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

