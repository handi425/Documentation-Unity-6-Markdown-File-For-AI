[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [HandleUtility](HandleUtility.html).RegisterRenderPickingCallback

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static bool
RegisterRenderPickingCallback([HandleUtility.RenderPickingCallback](HandleUtility.RenderPickingCallback.html)
renderPickingCallback);

### Parameters

renderPickingCallback | The delegate object to register to the callback.  
---|---  
  
### Returns

**bool** True if the registration succeeds. False if the callback is already
registered.

### Description

Registers a callback to invoke when Unity renders for picking.

Use this callback to render custom geometries on top of the existing scene
objects to the picking render texture, so that the GameObjects represented by
custom geometries can be picked.  
  
Each rendering must write out a [Vector4](Vector4.html)-typed `selectionId` to
the picking render texture. The `selectionId` is encoded from the
[pickingIndex](RenderPickingArgs-pickingIndex.html) passed into the callback
through the [RenderPickingArgs](RenderPickingArgs.html) struct using the
function
[HandleUtility.EncodeSelectionId](HandleUtility.EncodeSelectionId.html). You
can render multiple SelectionIds in one callback if they are encoded
sequentially from incrementing the `pickingIndex`, and you return the total
number of rendered picking indices when returning from the callback.  
  
Most Unity shaders have a "ScenePickingPass" pass that can be used for the
rendering. Use [Material.FindPass](Material.FindPass.html) with the pass name
"ScenePickingPass" to find the index of the shader pass from a
[Material](Material.html), and use this pass index when you call APIs such as
[Material.SetPass](Material.SetPass.html). Note that you can only use render
functions that are considered to take effect immediately, such as
[Graphics.DrawMeshNow](Graphics.DrawMeshNow.html) and
[Graphics.DrawProceduralNow](Graphics.DrawProceduralNow.html) (instead of
their non-immediate counterparts [Graphics.DrawMesh](Graphics.DrawMesh.html)
and [Graphics.DrawProcedural](Graphics.DrawProcedural.html)). The alternative
is to record your rendering to a [CommandBuffer](Rendering.CommandBuffer.html)
object, and call
[Graphics.ExecuteCommandBuffer](Graphics.ExecuteCommandBuffer.html) after the
recording.  
  
The picking render texture has already been bound as the active render texture
when it entered the callback. You can change the active render texture during
the callback, but you must restore the active render texture before exiting
the callback.  
  
Your rendering must respect the ignore and filter GameObject sets passed to
the callback through the [RenderPickingArgs](RenderPickingArgs.html) struct
argument to determine under the current context what should be rendered. Refer
to [RenderPickingArgs](RenderPickingArgs.html) for more information.  
  
After rendering, return a [RenderPickingResult](RenderPickingResult.html)
struct with the number of picking indices you used, and another callback
function to invoke to resolve the picking index to a GameObject reference to
be selected once the user ends up clicking on the rendered pixel under the
mouse. If nothing needs to render, you can return the struct with
[renderedPickingIndexCount](RenderPickingResult-
renderedPickingIndexCount.html) being 0, or simply
[RenderPickingResult.NoOperation](RenderPickingResult.NoOperation.html). Refer
to [RenderPickingResult](RenderPickingResult.html) for more information.  
  
The method throws `InvalidOperationException` if you try to call it inside
render picking callbacks.  
  
Additional resources:
[UnregisterRenderPickingCallback](HandleUtility.UnregisterRenderPickingCallback.html).

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

