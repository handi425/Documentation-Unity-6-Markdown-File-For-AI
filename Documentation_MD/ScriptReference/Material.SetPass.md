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

#  [Material](Material.html).SetPass

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

## Declaration

public bool SetPass(int pass);

### Parameters

pass | Shader pass number to setup.  
---|---  
  
### Returns

**bool** If false is returned, no rendering should be done.

### Description

Activate the given `pass` for rendering.

Pass indices start from zero and go up to (but not including)
[passCount](Material-passCount.html).  
  
This is mostly used in direct drawing code. For example, drawing 3D primitives
with [GL.Begin](GL.Begin.html), [GL.End](GL.End.html), and also drawing meshes
using [Graphics.DrawMeshNow](Graphics.DrawMeshNow.html).  
  
If SetPass returns false, you should not render anything. This is typically
the case for special pass types that aren't meant for rendering, like
[GrabPass](../Manual/SL-GrabPass.html).

    
    
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
                [Shader](Shader.html) shader = [Shader.Find](Shader.Find.html)("Hidden/Internal-Colored");
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
    

Additional resources: [passCount](Material-passCount.html) property,
[GL](GL.html) class, [ShaderLab documentation](../Manual/Shaders.html).

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

