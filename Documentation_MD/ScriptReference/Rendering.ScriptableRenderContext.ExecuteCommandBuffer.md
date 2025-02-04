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

#
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html).ExecuteCommandBuffer

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

public void
ExecuteCommandBuffer([Rendering.CommandBuffer](Rendering.CommandBuffer.html)
commandBuffer);

### Parameters

commandBuffer | Specifies the Command Buffer to execute.  
---|---  
  
### Description

Schedules the execution of a custom graphics Command Buffer.

During the call to
[ScriptableRenderContext.ExecuteCommandBuffer](Rendering.ScriptableRenderContext.ExecuteCommandBuffer.html),
[ScriptableRenderContext](Rendering.ScriptableRenderContext.html) registers
the commandBuffer parameter into its own internal list of commands to execute.
The actual execution of these commands (including the commands stored in the
custom commandBuffer) happens during
[ScriptableRenderContext.Submit](Rendering.ScriptableRenderContext.Submit.html).  
  
Make sure that you call ExecuteCommandBuffer before other
ScriptableRenderContext methods (such as DrawRenderers, DrawShadows) if your
draw calls depend on a state of the pipeline that you specify in a
CommandBuffer. The code sample below illustrates a case when commands are
submitted in an incorrect order ; followed by a case that behaves as expected:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    internal class ExecuteCommandBufferExample
    {
        // TODO: replace with actual settings
        [ScriptableRenderContext](Rendering.ScriptableRenderContext.html) scriptableRenderContext;
        [DrawingSettings](Rendering.DrawingSettings.html) drawingSettings;
        [CullingResults](Rendering.CullingResults.html) cullingResults = new [CullingResults](Rendering.CullingResults.html)();
        [FilteringSettings](Rendering.FilteringSettings.html) filteringSettings = new [FilteringSettings](Rendering.FilteringSettings.html)();  
      
        [Matrix4x4](Matrix4x4.html) myViewMatrix = [Matrix4x4.Scale](Matrix4x4.Scale.html)(new [Vector3](Vector3.html)(2f, 2f, 2f));  
      
        public void DrawRenderersExampleIncorrect()
        {
            [CommandBuffer](Rendering.CommandBuffer.html) myCommandBuffer = new [CommandBuffer](Rendering.CommandBuffer.html)();  
      
            myCommandBuffer.SetViewMatrix(myViewMatrix);  
      
            scriptableRenderContext.DrawRenderers(cullingResults, ref drawingSettings, ref filteringSettings);
            // NO! When scriptableRenderContext submits the DrawRenderers command, it will not know about myViewMatrix :(  
      
            scriptableRenderContext.ExecuteCommandBuffer(myCommandBuffer);
            myCommandBuffer.Clear();
        }  
      
        public void DrawRenderersExampleBetter()
        {
            [CommandBuffer](Rendering.CommandBuffer.html) myCommandBuffer = new [CommandBuffer](Rendering.CommandBuffer.html)();  
      
            myCommandBuffer.SetViewMatrix(myViewMatrix);  
      
            scriptableRenderContext.ExecuteCommandBuffer(myCommandBuffer);
            myCommandBuffer.Clear();  
      
            scriptableRenderContext.DrawRenderers(cullingResults, ref drawingSettings, ref filteringSettings);
            // OK! During next scriptableRenderContext.Submit() call, scriptableRenderContext will set myViewMatrix *before* drawing the renderers.
        }
    }
    

Additional resources: [CommandBuffer](Rendering.CommandBuffer.html).

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

