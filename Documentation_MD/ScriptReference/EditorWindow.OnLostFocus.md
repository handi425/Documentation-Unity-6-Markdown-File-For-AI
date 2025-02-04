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

#  [EditorWindow](EditorWindow.html).OnLostFocus()

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

Called when the window loses keyboard focus.

Additional resources: [OnFocus](EditorWindow.OnFocus.html).  
  
![](../StaticFiles/ScriptRefImages/OrthographicPreviewer.png)  
_Restores normal view when you lose focus on this window._

    
    
    // Simple script that lets you preview your main camera in
    // Orthographic view when selected.
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UIElements;
    
    public class OrthographicPreview : [EditorWindow](EditorWindow.html)
    {
        [RenderTexture](RenderTexture.html) renderTexture;
        [Camera](Camera.html) camera;
        [Image](UIElements.Image.html) image;
    
        [[MenuItem](MenuItem.html)("Examples/Orthographic Previewer")]
        static void Init()
        {
            OrthographicPreview window =
                (OrthographicPreview)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(OrthographicPreview), true, "My Empty Window");
            window.Show();
        }
    
        void OnEnable()
        {
            int w = (int)this.position.width;
            int h = (int)this.position.height;
    
            image = new [Image](UIElements.Image.html)();
            renderTexture = new [RenderTexture](RenderTexture.html)(w, h, 32, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            camera = [Camera.main](Camera-main.html);
        }
        
        void OnDisable()
        {
            [Object.DestroyImmediate](Object.DestroyImmediate.html)(renderTexture);
        }
    
        void CreateGUI()
        {
            var buttonClose = new [Button](UIElements.Button.html)();
            buttonClose.text = "Close";
            buttonClose.clicked += () =>
            {
                camera.orthographic = false;
                this.Close();
            };
            rootVisualElement.Add(buttonClose);
    
            if (renderTexture != null)
            {
                image.image = renderTexture;
                rootVisualElement.Add(image);          
            }
        }
    
        void OnFocus()
        {
            [Selection.activeTransform](Selection-activeTransform.html) = camera.transform;
            camera.orthographic = true;
        }
    
        void [Update](PlayerLoop.Update.html)()
        {
            int w = (int)this.position.width;
            int h = (int)this.position.height;
            if (renderTexture.width != w || renderTexture.height != h)
            {
                [Object.DestroyImmediate](Object.DestroyImmediate.html)(renderTexture);
                renderTexture = new [RenderTexture](RenderTexture.html)(w, h, 32, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
                image.image = renderTexture;
            }
    
            if (camera != null)
            {
                camera.targetTexture = renderTexture;
                camera.Render();
                camera.targetTexture = null;
            }
        }
    
        void OnLostFocus()
        {
            camera.orthographic = false;
        }
    }
    

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

