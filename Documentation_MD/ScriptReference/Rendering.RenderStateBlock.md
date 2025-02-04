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

# RenderStateBlock

struct in UnityEngine.Rendering

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

A set of values that Unity uses to override the GPU's render state.

When you call ScriptableRenderContext.DrawRenderers, you can use this to
override the render state for some or all of the geometry.  
  
**Note:** You must set [mask](Rendering.RenderStateBlock-mask.html) to tell
Unity which parts of the render state to override to apply. For example, to
apply the values in [blendState](Rendering.RenderStateBlock-blendState.html),
[mask](Rendering.RenderStateBlock-mask.html) must include
[RenderStateMask.Blend](Rendering.RenderStateMask.Blend.html).

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    public class OverrideRenderStateExample
    {
        [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) scriptableRenderContext;  
      
        // Placeholder data
        [DrawingSettings](Rendering.DrawingSettings.html) exampleDrawingSettings;
        [CullingResults](Rendering.CullingResults.html) exampleCullingResults = new [CullingResults](Rendering.CullingResults.html)();
        [FilteringSettings](Rendering.FilteringSettings.html) exampleFilteringSettings = new [FilteringSettings](Rendering.FilteringSettings.html)();  
      
        public void OverrideRenderState()
        {
            // Tell Unity how to override the render state when it draws the geometry.
            var stateBlock = new [RenderStateBlock](Rendering.RenderStateBlock.html)([RenderStateMask.Depth](Rendering.RenderStateMask.Depth.html));
            stateBlock.depthState = new [DepthState](Rendering.DepthState.html)(true, [CompareFunction.LessEqual](Rendering.CompareFunction.LessEqual.html));  
      
            // Schedule the drawing operation.
            scriptableRenderContext.DrawRenderers(exampleCullingResults, ref exampleDrawingSettings, ref exampleFilteringSettings, ref stateBlock);  
      
            // Perform all scheduled tasks, in the order that they were scheduled.
            scriptableRenderContext.Submit();
        }
    }
    

Additional resources: ScriptableRenderContext.DrawRenderers,
[RenderStateMask](Rendering.RenderStateMask.html).

### Properties

[blendState](Rendering.RenderStateBlock-blendState.html)| Specifies the new
blend state.  
---|---  
[depthState](Rendering.RenderStateBlock-depthState.html)| Specifies the new
depth state.  
[mask](Rendering.RenderStateBlock-mask.html)| Specifies which parts of the
GPU's render state to override.  
[rasterState](Rendering.RenderStateBlock-rasterState.html)| Specifies the new
raster state.  
[stencilReference](Rendering.RenderStateBlock-stencilReference.html)| The
value to be compared against and/or the value to be written to the buffer,
based on the stencil state.  
[stencilState](Rendering.RenderStateBlock-stencilState.html)| Specifies the
new stencil state.  
  
### Constructors

[RenderStateBlock](Rendering.RenderStateBlock-ctor.html)| Creates a new render
state block with the specified mask.  
---|---  
  
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

