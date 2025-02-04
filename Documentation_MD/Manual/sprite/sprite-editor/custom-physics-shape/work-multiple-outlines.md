[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/custom-physics-shape/work-multiple-outlines.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite editor](../../../sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom physics shape](../../../sprite/sprite-editor/custom-physics-shape/custom-physics-shape-landing.html)
  * Work with multiple outlines

[](../../../sprite/sprite-editor/custom-physics-shape/move-edges.html)

Move edges

[](../../../sprite/sprite-editor/custom-physics-shape/update-shape-
collider-2d-meshes.html)

Update the shape of the collider 2D meshes

# Work with multiple outlines

A **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites
are essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite)’s physics shape can contain
multiple separate outlines. This is useful if only specific areas of a Sprite
need a **Collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collider) 2D **Mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](../../../mesh.html)  
See in [Glossary](../../../Glossary.html#Mesh) for **collision** A collision
occurs when the physics engine detects that the colliders of two GameObjects
make contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](../../../CollidersOverview.html)  
See in [Glossary](../../../Glossary.html#Collision). For example, you might
want a character to only respond to collisions on specific areas of its Sprite
as part of your game’s damage mechanic.

To create a new rectangular outline with four control points, click and drag
over any empty space in the Sprite Editor window. Repeat this step to create
additional outlines. You can refine each outline in the same way you would for
a single Physics Shape outline.

![](../../../../uploads/Main/2D-CustomPS-generatedoutline-multi1.png) | ![](../../../../uploads/Main/2D-CustomPS-generatedoutline-multi2.png)  
---|---  
Fig. 1: Click and drag to create a four-point box. | Fig. 2: Box physics shape with four control points.  
![](../../../../uploads/Main/2D-CustomPS-generatedoutline-multi3.png) | ![](../../../../uploads/Main/2D-CustomPS-generatedoutline-multi4.png)  
Fig. 3: Click and drag again for another box. | Fig. 4: Repeat to create more separate outlines.  
  
[](../../../sprite/sprite-editor/custom-physics-shape/move-edges.html)

Move edges

[](../../../sprite/sprite-editor/custom-physics-shape/update-shape-
collider-2d-meshes.html)

Update the shape of the collider 2D meshes

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

