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

# WaitForEndOfFrame

class in UnityEngine

/

Inherits from:[YieldInstruction](YieldInstruction.html)

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

Waits until the end of the frame after Unity has rendered every Camera and
GUI, just before displaying the frame on screen.

You can use it to read the display into a Texture, encode it as an image file
(see [Texture2D.ReadPixels](Texture2D.ReadPixels.html) and
[Texture2D.Texture2D](Texture2D.EncodeToPNG.html)) and store it on a device.  
  
Switching from the Game view to the Scene view causes
[WaitForEndOfFrame](WaitForEndOfFrame.html) to freeze. It only continues when
the application switches back to the Game view. This can only happen when the
application is working in the Unity editor.  
  
**Note:** This coroutine is not invoked on the editor in batch mode. For
further details please look at the [Command line
arguments](../Manual/CommandLineArguments.html) page in the manual.

    
    
    using System.IO;
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Take a shot immediately
        IEnumerator Start()
        {
            UploadPNG();
            yield return null;
        }  
      
        IEnumerator UploadPNG()
        {
            // We should only read the screen buffer after rendering is complete
            yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();  
      
            // Create a texture the size of the screen, RGB24 format
            int width = [Screen.width](Screen-width.html);
            int height = [Screen.height](Screen-height.html);
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html)(width, height, [TextureFormat.RGB24](TextureFormat.RGB24.html), false);  
      
            // Read screen contents into the texture
            tex.ReadPixels(new [Rect](Rect.html)(0, 0, width, height), 0, 0);
            tex.Apply();  
      
            // Encode texture into PNG
            byte[] bytes = tex.EncodeToPNG();
            Destroy(tex);  
      
            // For testing purposes, also write to a file in the project folder
            // [File.WriteAllBytes](Windows.File.WriteAllBytes.html)([Application.dataPath](Application-dataPath.html) + "/../SavedScreen.png", bytes);  
      
    
            // Create a Web Form
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();
            form.AddField("frameCount", Time.frameCount.ToString());
            form.AddBinaryData("fileUpload", bytes);  
      
            // Upload to a cgi script
            var w = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("http://localhost/cgi-bin/env.cgi?post", form);
            yield return w.SendWebRequest();
            if (w.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                print(w.error);
            else
                print("Finished Uploading Screenshot");
            yield return null;
        }
    }
    
    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // A script that shows destination alpha channel in the game view.  
      
        [Material](Material.html) mat;  
      
        void CreateMaterial()
        {
            // Unity has a built-in shader that is useful for drawing
            // simple colored things. In this case, we just want to use
            // a blend mode that inverts destination colors.
            var shader = [Shader.Find](Shader.Find.html)("Hidden/Internal-Colored");
            mat = new [Material](Material.html)(shader);
            mat.hideFlags = [HideFlags.HideAndDontSave](HideFlags.HideAndDontSave.html);
            // Set blend mode to show destination alpha channel.
            mat.SetInt("_SrcBlend", (int)UnityEngine.Rendering.BlendMode.DstAlpha);
            mat.SetInt("_DstBlend", (int)UnityEngine.Rendering.BlendMode.Zero);
            // Turn off backface culling, depth writes, depth test.
            mat.SetInt("_Cull", (int)UnityEngine.Rendering.CullMode.Off);
            mat.SetInt("_ZWrite", 0);
            mat.SetInt("_ZTest", (int)UnityEngine.Rendering.CompareFunction.Always);
        }  
      
        public IEnumerator Start()
        {
            CreateMaterial();
            while (true)
            {
                // Wait until all rendering + UI is done.
                yield return new [WaitForEndOfFrame](WaitForEndOfFrame.html)();
                // Draw a quad that shows alpha channel.
                [GL.PushMatrix](GL.PushMatrix.html)();
                [GL.LoadOrtho](GL.LoadOrtho.html)();
                mat.SetPass(0);
                [GL.Begin](GL.Begin.html)([GL.QUADS](GL.QUADS.html));
                [GL.Vertex3](GL.Vertex3.html)(0, 0, 0);
                [GL.Vertex3](GL.Vertex3.html)(1, 0, 0);
                [GL.Vertex3](GL.Vertex3.html)(1, 1, 0);
                [GL.Vertex3](GL.Vertex3.html)(0, 1, 0);
                [GL.End](GL.End.html)();
                [GL.PopMatrix](GL.PopMatrix.html)();
            }
            yield return null;
        }
    }
    

Additional resources: [AsyncOperation](AsyncOperation.html),
[WaitForSeconds](WaitForSeconds.html),
[WaitForFixedUpdate](WaitForFixedUpdate.html),
[WaitForSecondsRealtime](WaitForSecondsRealtime.html),
[WaitUntil](WaitUntil.html),[WaitWhile](WaitWhile.html).

### Inherited Members

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

