[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/custom-outline-editor/custom-outline-editor-reference.html)

  * [Working in Unity](../../../working-in-unity.html)
  * [2D in Unity](../../../Unity2D.html)
  * [Sprites](../../../sprite/sprite-landing.html)
  * [Sprite editor](../../../sprite/sprite-editor/sprite-editor-landing.html)
  * [Custom outline](../../../sprite/sprite-editor/custom-outline-editor/custom-outline-editor-landing.html)
  * Custom outline editor reference

[](../../../sprite/sprite-editor/custom-outline-editor/move-edges.html)

Move edges

[](../../../sprite/sprite-editor/custom-physics-shape/custom-physics-shape-
landing.html)

Custom physics shape

# Custom outline editor reference

Property | Function  
---|---  
**Snap** | Snap control points to the nearest **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../../ShadowPerformance.html)  
See in [Glossary](../../../Glossary.html#pixel).  
**Outline Tolerance** | Use this slider to control how tightly and accurately the generated outline follows the outline of the **Sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](../../../sprite/sprite-landing.html)  
See in [Glossary](../../../Glossary.html#Sprite) texture. At the minimum value
(0), the Sprite Editor generates a basic outline around the Sprite. At the
maximum value (1), the Sprite Editor generates an outline that follows the
outline of the Sprite texture as closely as possible.  
**Generate** | When you click this button, Unity automatically creates an outline based on the **Outline Tolerance** value you set.  
**Copy** | After you have generated or set up a custom outline, click this **Copy** button to duplicate the custom outline. Leaving the Custom outline module or closing the Sprite Editor removes the copied outline from memory.  
**Paste** | Use this button to paste a copied outline to the currently selected Sprite. If you have not used the **Copy** function to copy an outline, this button is not available. To **Paste** a copied custom outline to another Sprite, in the **Project window** A window that shows the contents of your `Assets` folder (Project tab) [More info](../../../ProjectView.html)  
See in [Glossary](../../../Glossary.html#Projectwindow) select the Sprite
while the Custom outline editor window is open. Then click the **Paste**
button to paste the copied outline to the new Sprite. When you paste the
outline, if a point in the outline is larger than the Sprite’s frame, Unity
clamps the point to be inside the Sprite’s frame.  
**Paste All** | Use this button to paste a copied outline to all sprites in the Sprite Editor window, regardless of selection. If you have not used the **Copy** function to copy an outline, this button is unavailable. Use this function to apply the same outline to multiple sprites in the same Texture (such as when a Texture has its [Sprite Mode](../../../texture-type-sprite.html) set to ‘Multiple’). When you paste the outline, if a point in the outline exceeds the Sprite’s frame, Unity clamps the point to be inside that Sprite’s frame.  
**Revert** | Undoes any unsaved recent changes made in the editor window. To save changes, click **Apply** first.  
**Apply** | Select this button to save all changes made in the editor window.  
  
[](../../../sprite/sprite-editor/custom-outline-editor/move-edges.html)

Move edges

[](../../../sprite/sprite-editor/custom-physics-shape/custom-physics-shape-
landing.html)

Custom physics shape

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

