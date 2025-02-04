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

#  [EditorGUIUtility](EditorGUIUtility.html).whiteTexture

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

public static [Texture2D](Texture2D.html) whiteTexture;

### Description

Get a white texture.

![](../StaticFiles/ScriptRefImages/EditorGUIUtilityWhiteTexture.png)  
_White texture in an Editor Window._

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUITextures : [EditorWindow](EditorWindow.html)
    {
        [Texture2D](Texture2D.html) texture = null;
        static [Texture2D](Texture2D.html) invertedTexture;
        bool showInverted = false;  
      
        [[MenuItem](MenuItem.html)("Examples/[Texture](Texture.html) Previewer")]
        static void Init()
        {
            EditorGUITextures window =
                [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<EditorGUITextures>(new [Rect](Rect.html)(0, 0, 410, 250));
            window.Show();
        }  
      
        void OnGUI()
        {
            texture = ([Texture2D](Texture2D.html))[EditorGUI.ObjectField](EditorGUI.ObjectField.html)(new [Rect](Rect.html)(3, 3, 200, 50),
                "Add a [Texture](Texture.html):",
                texture,
                typeof([Texture](Texture.html)));  
      
    
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(250, 3, 100, 20), "Process Inverted"))
            {
                if (invertedTexture)
                    DestroyImmediate(invertedTexture);  
      
                //Copy the new texture
                invertedTexture = new [Texture2D](Texture2D.html)(texture.width,
                    texture.height,
                    texture.format,
                    (texture.mipmapCount != 0));  
      
                for (int m = 0; m < texture.mipmapCount; m++)
                    invertedTexture.SetPixels(texture.GetPixels(m), m);  
      
                InvertColors();
                showInverted = true;
            }  
      
            if (texture)
            {
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(25, 200, 100, 25), new [GUIContent](GUIContent.html)("Preview:"));
                [EditorGUI.DrawPreviewTexture](EditorGUI.DrawPreviewTexture.html)(new [Rect](Rect.html)(25, 70, 100, 100), texture);
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(150, 200, 100, 25), new [GUIContent](GUIContent.html)("Alpha:"));
                [EditorGUI.DrawTextureAlpha](EditorGUI.DrawTextureAlpha.html)(new [Rect](Rect.html)(150, 70, 100, 100), texture);
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(275, 200, 100, 25), new [GUIContent](GUIContent.html)("Inverted:"));  
      
                if (showInverted)
                {
                    [EditorGUI.DrawPreviewTexture](EditorGUI.DrawPreviewTexture.html)(new [Rect](Rect.html)(275, 70, 100, 100), invertedTexture);
                }  
      
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, position.height - 25, position.width - 6, 20), "Clear texture"))
                {
                    texture = [EditorGUIUtility.whiteTexture](EditorGUIUtility-whiteTexture.html);
                    showInverted = false;
                }
            }
            else
            {
                [EditorGUI.PrefixLabel](EditorGUI.PrefixLabel.html)(
                    new [Rect](Rect.html)(3, position.height - 25, position.width - 6, 20),
                    0,
                    new [GUIContent](GUIContent.html)("No texture found"));
            }
        }  
      
        static void InvertColors()
        {
            for (int m = 0; m < invertedTexture.mipmapCount; m++)
            {
                [Color](Color.html)[] c = invertedTexture.GetPixels(m);
                for (int i = 0; i < c.Length; i++)
                {
                    c[i].r = 1 - c[i].r;
                    c[i].g = 1 - c[i].g;
                    c[i].b = 1 - c[i].b;
                }
                invertedTexture.SetPixels(c, m);
            }
            invertedTexture.Apply();
        }  
      
        void OnInspectorUpdate()
        {
            this.Repaint();
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

