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

#  [MonoBehaviour](MonoBehaviour.html).OnPostRender()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

[Event function](../Manual/event-functions.html) that Unity calls after a
Camera renders the scene.

In the Built-in Render Pipeline, Unity calls `OnPostRender` on MonoBehaviours
that are attached to the same GameObject as an enabled [Camera](Camera.html)
component, just after that Camera renders the scene. Use `OnPostRender` to
execute your own code at this point in the render loop; for example, if you
changed a visual effect in
[MonoBehaviour.OnPreRender](MonoBehaviour.OnPreRender.html), you can change it
back here. `OnPostRender` can be a coroutine.  
  
For similar functionality that does not require the script to be on the same
GameObject as a Camera component, see [Camera.onPostRender](Camera-
onPostRender.html). For similar functionality in the Scriptable Render
Pipeline, see [RenderPipelineManager](Rendering.RenderPipelineManager.html).  
  
To execute code after Unity renders all Cameras and GUI, use
[WaitForEndOfFrame](WaitForEndOfFrame.html) or a
[CommandBuffer](Rendering.CommandBuffer.html).

    
    
    using UnityEngine;  
      
    // A script that when attached to the camera, makes the resulting
    // colors inverted. See its effect in play mode.
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Material](Material.html) mat;  
      
        // Will be called from camera after regular rendering is done.
        public void OnPostRender()
        {
            if (!mat)
            {
                // Unity has a built-in shader that is useful for drawing
                // simple colored things. In this case, we just want to use
                // a blend mode that inverts destination colors.
                var shader = [Shader.Find](Shader.Find.html)("Hidden/Internal-Colored");
                mat = new [Material](Material.html)(shader);
                mat.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
                // Set blend mode to invert destination colors.
                mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusDstColor);
                mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.Zero);
                // Turn off backface culling, depth writes, depth test.
                mat.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
                mat.SetInt("_ZWrite", 0);
                mat.SetInt("_ZTest", (int)UnityEngine.Rendering.CompareFunction.Always);
            }  
      
            [GL.PushMatrix](GL.PushMatrix.html)();
            [GL.LoadOrtho](GL.LoadOrtho.html)();  
      
            // activate the first shader pass (in this case we know it is the only pass)
            mat.SetPass(0);
            // draw a quad over whole screen
            [GL.Begin](GL.Begin.html)([GL.QUADS](GL.QUADS.html));
            [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(1, 0, 0);
            [GL.Vertex3](GL.Vertex3.html)(1, 1, 0);
            [GL.Vertex3](GL.Vertex3.html)(0, 1, 0);
            [GL.End](GL.End.html)();  
      
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

Additional resources: [Camera.onPostRender](Camera-onPostRender.html),
[MonoBehaviour.OnPreRender](MonoBehaviour.OnPreRender.html),
[MonoBehaviour.OnPreCull](MonoBehaviour.OnPreCull.html),
[CommandBuffer](Rendering.CommandBuffer.html), [Extending the Built-in Render
Pipeline using CommandBuffers](../Manual/GraphicsCommandBuffers.html),
[WaitForEndOfFrame](WaitForEndOfFrame.html).

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

