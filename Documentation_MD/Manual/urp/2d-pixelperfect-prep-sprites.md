[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-prep-sprites.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [中文](/cn/current/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [日本語](/ja/current/Manual/urp/2d-pixelperfect-prep-sprites.html)
  * [한국어](/kr/current/Manual/urp/2d-pixelperfect-prep-sprites.html)

  * [Working in Unity](../working-in-unity.html)
  * [2D in Unity](../Unity2D.html)
  * [2D game development in URP](../2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](../urp/2d-pixelperfect.html)
  * Prepare your sprites for the 2D Pixel Perfect Camera in URP

[](../urp/2d-pixelperfect-intro.html)

Introduction to the Pixel Perfect Camera in URP

[](../urp/pixel-cinemachine.html)

Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

# Prepare your sprites for the 2D Pixel Perfect Camera in URP

Set up your **sprites** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../sprite/sprite-landing.html)  
See in [Glossary](../Glossary.html#Sprite) for compatibility with the
**Pixel** The smallest unit in a computer image. Pixel size depends on your
screen resolution. Pixel lighting is calculated at every screen pixel. [More
info](../ShadowPerformance.html)  
See in [Glossary](../Glossary.html#pixel) Perfect **Camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](../CamerasOverview.html)  
See in [Glossary](../Glossary.html#Camera) component.

  1. After importing your asset into the project as sprites, set all sprites to the same **Pixels Per Unit** value.  
![Setting PPU value](../../uploads/urp/2D/2D_Pix_image_1.png)

  2. In the sprites’ **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../UsingTheInspector.html)  
See in [Glossary](../Glossary.html#Inspector) window, open the **Filter Mode**
dropdown and select **Point**.  
![Set Point mode](../../uploads/urp/2D/2D_Pix_image_2.png)

  3. Open the ****Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](class-TextureImporterOverride), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](../Glossary.html#compression)** dropdown and select
**None**.  
![Set None compression](../../uploads/urp/2D/2D_Pix_image_3.png)

Follow the steps below to set the pivot for a sprite:

  1. Open the **Sprite Editor** window for the selected sprite.

  2. If the sprite’s **Sprite Mode** is set to **Multiple** and there are multiple individual sprite elements in the imported texture, then you need to set a pivot point for each individual sprite element.

  3. In the Sprite panel at the lower left of the **Sprite Editor** window, open the **Pivot** dropdown and select **Custom**. Then open the **Pivot Unit Mode** and select **Pixels**. This allows you to set the pivot point’s coordinates in pixels, or drag the pivot point around in the **Sprite Editor** and have it automatically snap to pixel corners.  
![Setting the Sprite’s Pivot](../../uploads/urp/2D/2D_Pix_image_4.png)

  4. Repeat step 3 for each sprite element as necessary.

## Set up snap settings

Follow the steps below to set the snap settings for your project to ensure
that the movement of pixelated sprites are consistent with each other:

  1. To open the **Increment Snapping** settings, go to **Grid and Snap Overlay** in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](../CreatingScenes.html)  
See in [Glossary](../Glossary.html#Scene) view.  
![Snap Setting window](../../uploads/urp/2D/2D_Pix_image_5.png)

  2. Set the **Move X/Y/Z** properties to 1 divided by the Pixel Perfect Camera’s **Asset Pixels Per Unit (PPU)** value. For example, if the Asset **PPU** is 100, you should set the **Move X/Y/Z** properties to 0.01 (1 / 100 = 0.01).  
![Grid Snap Setting window](../../uploads/urp/2D/2D_Pix_image_6.png)

  3. Select the **Grid Snapping** icon to enable it (highlighted in blue).

  4. Unity does not apply Snap settings retroactively. If there are any pre-existing **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../class-GameObject.html)  
See in [Glossary](../Glossary.html#GameObject) in the scene, select each of
them and select **All Axes** to apply the updated Snap settings.

[](../urp/2d-pixelperfect-intro.html)

Introduction to the Pixel Perfect Camera in URP

[](../urp/pixel-cinemachine.html)

Make Cinemachine compatible with the 2D Pixel Perfect camera in URP

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

