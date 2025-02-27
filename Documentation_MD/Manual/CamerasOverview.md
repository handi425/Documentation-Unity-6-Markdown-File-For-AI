[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CamerasOverview.html)
  * [中文](/cn/current/Manual/CamerasOverview.html)
  * [日本語](/ja/current/Manual/CamerasOverview.html)
  * [한국어](/kr/current/Manual/CamerasOverview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CamerasOverview.html)
  * [中文](/cn/current/Manual/CamerasOverview.html)
  * [日本語](/ja/current/Manual/CamerasOverview.html)
  * [한국어](/kr/current/Manual/CamerasOverview.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * Introduction to cameras

[](Cameras.html)

Cameras

[](CameraView.html)

The camera view

# Introduction to cameras

Just as cameras are used in films to display the story to the audience,
**Cameras** in Unity are used to display the game world to the player.

A Unity **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) represents **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a three-dimensional space.
Since the viewer’s screen is two-dimensional, Unity needs to capture a view
and “flatten” it for display. It does this using cameras.

Cameras can be customized, scripted, or parented to achieve just about any
kind of effect imaginable. For a puzzle game, you might keep the Camera static
for a full view of the puzzle. For a first-person shooter, you would parent
the Camera to the player character, and place it at the character’s eye level.
For a racing game, you’d probably have the Camera follow your player’s
vehicle.

By customizing and manipulating cameras, you can make the presentation of your
game truly unique. You will always have at least one camera in a scene, but
you can have more than one. You can have an unlimited number of cameras in a
scene. They can be set to render in any order, at any place on the screen, or
only certain parts of the screen.

In Unity, you create a camera by adding a [Camera component](class-
Camera.html) to a GameObject.

## Perspective and orthographic cameras

![The same scene shown in perspective mode \(left\) and orthographic mode
\(right\) ](../uploads/Main/CameraPerspectiveAndOrtho.jpg) The same scene
shown in perspective mode (left) and orthographic mode (right)

A camera in the real world, or indeed a human eye, sees the world in a way
that makes objects look smaller the farther they are from the point of view.
This well-known _perspective_ effect is widely used in art and computer
graphics and is important for creating a realistic scene. Naturally, Unity
supports perspective cameras, but for some purposes, you want to render the
view without this effect. For example, you might want to create a map or
information display that is not supposed to appear exactly like a real-world
object. A camera that does not diminish the size of objects with distance is
referred to as _orthographic_ and Unity cameras also have an option for this.
The perspective and orthographic modes of viewing a scene are known as camera
_projections_. _(scene above
from[BITGEM](https://www.assetstore.unity3d.com/en/#!/publisher/1299))_

Marking a Camera as **Orthographic** removes all perspective from the Camera’s
view. This is mostly useful for making isometric or 2D games.

Note that fog is rendered uniformly in orthographic camera mode and may
therefore not appear as expected. This is because the Z coordinate of the
post-perspective space is used for the fog “depth”. This is not strictly
accurate for an orthographic camera but it is used for its performance
benefits during rendering.

## Render path

Unity supports different rendering paths. You should choose which one you use
depending on your game content and target platform / hardware. Different
rendering paths have different features and performance characteristics that
mostly affect lights and shadows. The rendering path used by your Project is
chosen in the **Player** settings. Additionally, you can override it for each
Camera.

For more information on rendering paths, check the [rendering
paths](RenderingPaths.html)The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) page.

## Additional resources

  * [Introduction to cameras in URP](urp/cameras/camera-differences-in-urp.html)
  * [Camera render types in URP](urp/camera-types-and-render-type.html)
  * [Camera render order in URP](urp/cameras-advanced.html)
  * [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

[](Cameras.html)

Cameras

[](CameraView.html)

The camera view

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

