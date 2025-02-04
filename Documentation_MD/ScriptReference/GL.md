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

# GL

class in UnityEngine

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

Low-level graphics library.

Use this class to manipulate active transformation matrices, issue rendering
commands similar to OpenGL's immediate mode and do other low-level graphics
tasks. Note that in almost all cases using
[Graphics.RenderMesh](Graphics.RenderMesh.html) or
[CommandBuffer](Rendering.CommandBuffer.html) is more efficient than using
immediate mode drawing.  
  
GL immediate drawing functions use whatever is the "current material" set up
right now (see [Material.SetPass](Material.SetPass.html)). The material
controls how the rendering is done (blending, textures, etc.), so unless you
explicitly set it to something before using GL draw functions, the material
can happen to be anything. Also, if you call any other drawing commands from
inside GL drawing code, they can set material to something else, so make sure
it's under control as well.  
  
GL drawing commands execute immediately. That means if you call them in
Update(), they will be executed before the camera is rendered (and the camera
will most likely clear the screen, making the GL drawing not visible).  
  
The usual place to call GL drawing is most often in
[OnPostRender](Camera.OnPostRender.html)() from a script attached to a camera,
or inside an image effect function
([OnRenderImage](Camera.OnRenderImage.html)).  
  
**Note:** The High Definition Render Pipeline (HDRP) and the Universal Render
Pipeline (URP) do not support [OnPostRender](Camera.OnPostRender.html).
Instead, use
[RenderPipelineManager.endCameraRendering](Rendering.RenderPipelineManager-
endCameraRendering.html) or
[RenderPipelineManager.endFrameRendering](Rendering.RenderPipelineManager-
endFrameRendering.html).  
  

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // When added to an object, draws colored rays from the
        // transform position.
        public int lineCount = 100;
        public float radius = 3.0f;  
      
        static [Material](Material.html) lineMaterial;
        static void CreateLineMaterial()
        {
            if (!lineMaterial)
            {
                // Unity has a built-in shader that is useful for drawing
                // simple colored things.
                [Shader](Shader.html) shader = [Shader.Find](Shader.Find.html)("Hidden/Internal-Colored");
                lineMaterial = new [Material](Material.html)(shader);
                lineMaterial.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
                // Turn on alpha blending
                lineMaterial.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.SrcAlpha);
                lineMaterial.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.OneMinusSrcAlpha);
                // Turn backface culling off
                lineMaterial.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
                // Turn off depth writes
                lineMaterial.SetInt("_ZWrite", 0);
            }
        }  
      
        // Will be called after all regular rendering is done
        public void OnRenderObject()
        {
            CreateLineMaterial();
            // Apply the line material
            lineMaterial.SetPass(0);  
      
            [GL.PushMatrix](GL.PushMatrix.html)();
            // Set transformation matrix for drawing to
            // match our transform
            [GL.MultMatrix](GL.MultMatrix.html)(transform.localToWorldMatrix);  
      
            // Draw lines
            [GL.Begin](GL.Begin.html)([GL.LINES](GL.LINES.html));
            for (int i = 0; i < lineCount; ++i)
            {
                float a = i / (float)lineCount;
                float angle = a * [Mathf.PI](Mathf.PI.html) * 2;
                // [Vertex](UIElements.Vertex.html) colors change from red to green
                [GL.Color](GL.Color.html)(new [Color](Color.html)(a, 1 - a, 0, 0.8F));
                // One vertex at transform position
                [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
                // Another vertex at edge of circle
                [GL.Vertex3](GL.Vertex3.html)([Mathf.Cos](Mathf.Cos.html)(angle) * radius, [Mathf.Sin](Mathf.Sin.html)(angle) * radius, 0);
            }
            [GL.End](GL.End.html)();
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

**Note:** This class is almost always used when you need to draw a couple of
lines or triangles, and don't want to deal with meshes. If you want to avoid
surprises the usage pattern is this:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnPostRender()
        {
            // Set your materials
            [GL.PushMatrix](GL.PushMatrix.html)();
            // yourMaterial.SetPass( );
            // Draw your stuff
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

Where at the "// Draw your stuff" you should do SetPass() on some material
previously declared, which will be used for drawing. If you dont call SetPass,
then you'll get basically a random material (whatever was used before) which
is not good. So do it.

### Static Properties

[invertCulling](GL-invertCulling.html)| Select whether to invert the backface
culling (true) or not (false).  
---|---  
[LINE_STRIP](GL.LINE_STRIP.html)| Mode for Begin: draw line strip.  
[LINES](GL.LINES.html)| Mode for Begin: draw lines.  
[modelview](GL-modelview.html)| Gets or sets the modelview matrix.  
[QUADS](GL.QUADS.html)| Mode for Begin: draw quads.  
[sRGBWrite](GL-sRGBWrite.html)| Controls whether Linear-to-sRGB color
conversion is performed while rendering.  
[TRIANGLE_STRIP](GL.TRIANGLE_STRIP.html)| Mode for Begin: draw triangle strip.  
[TRIANGLES](GL.TRIANGLES.html)| Mode for Begin: draw triangles.  
[wireframe](GL-wireframe.html)| Should rendering be done in wireframe?  
  
### Static Methods

[Begin](GL.Begin.html)| Begin drawing 3D primitives.  
---|---  
[Clear](GL.Clear.html)| Clear the current render buffer.  
[ClearWithSkybox](GL.ClearWithSkybox.html)| Clear the current render buffer
with camera's skybox.  
[Color](GL.Color.html)| Sets current vertex color.  
[End](GL.End.html)| End drawing 3D primitives.  
[Flush](GL.Flush.html)| Sends queued-up commands in the driver's command
buffer to the GPU.  
[GetGPUProjectionMatrix](GL.GetGPUProjectionMatrix.html)| Compute GPU
projection matrix from camera's projection matrix.  
[InvalidateState](GL.InvalidateState.html)| Invalidate the internally cached
render state.  
[IssuePluginEvent](GL.IssuePluginEvent.html)| Send a user-defined event to a
native code plugin.  
[LoadIdentity](GL.LoadIdentity.html)| Load an identity into the current model
and view matrices.  
[LoadOrtho](GL.LoadOrtho.html)| Helper function to set up an orthograhic
projection.  
[LoadPixelMatrix](GL.LoadPixelMatrix.html)| Setup a matrix for pixel-correct
rendering.  
[LoadProjectionMatrix](GL.LoadProjectionMatrix.html)| Load an arbitrary matrix
to the current projection matrix.  
[MultiTexCoord](GL.MultiTexCoord.html)| Sets current texture coordinate
(v.x,v.y,v.z) to the actual texture unit.  
[MultiTexCoord2](GL.MultiTexCoord2.html)| Sets current texture coordinate
(x,y) for the actual texture unit.  
[MultiTexCoord3](GL.MultiTexCoord3.html)| Sets current texture coordinate
(x,y,z) to the actual texture unit.  
[MultMatrix](GL.MultMatrix.html)| Sets the current model matrix to the one
specified.  
[PopMatrix](GL.PopMatrix.html)| Restores the model, view and projection
matrices off the top of the matrix stack.  
[PushMatrix](GL.PushMatrix.html)| Saves the model, view and projection
matrices to the top of the matrix stack.  
[RenderTargetBarrier](GL.RenderTargetBarrier.html)| Resolves the render target
for subsequent operations sampling from it.  
[TexCoord](GL.TexCoord.html)| Sets current texture coordinate (v.x,v.y,v.z)
for all texture units.  
[TexCoord2](GL.TexCoord2.html)| Sets current texture coordinate (x,y) for all
texture units.  
[TexCoord3](GL.TexCoord3.html)| Sets current texture coordinate (x,y,z) for
all texture units.  
[Vertex](GL.Vertex.html)| Submit a vertex.  
[Vertex3](GL.Vertex3.html)| Submit a vertex.  
[Viewport](GL.Viewport.html)| Set the rendering viewport.  
  
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

