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

#  [EditorUtility](EditorUtility.html).FocusProjectWindow

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

public static void FocusProjectWindow();

### Description

Brings the project window to the front and focuses it.

This is commonly called after a menu item that creates and selects an asset is
invoked.  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityFocusProjectWindow.png)  
_Changes the color of the selected GameObjects._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class FocusProjectWindowExample : [EditorWindow](EditorWindow.html)
    {
        static [Color](Color.html)    matColor = [Color.white](Color-white.html);  
      
    
        [[MenuItem](MenuItem.html)("Example/[Color](Color.html) Change")]
        static void Init()
        {
            // Get existing open window or if none, make a new one:
            FocusProjectWindowExample window = (FocusProjectWindowExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(FocusProjectWindowExample));
            window.Show();
        }  
      
        void OnGUI()
        {
            matColor = [EditorGUI.ColorField](EditorGUI.ColorField.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 15), "New [Color](Color.html):", matColor);
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 30), "Change"))
                ChangeColors();
        }  
      
        void ChangeColors()
        {
            if ([Selection.activeGameObject](Selection-activeGameObject.html))
            {
                foreach ([GameObject](GameObject.html) t in [Selection.gameObjects](Selection-gameObjects.html))
                {
                    [Renderer](Renderer.html) rend = t.GetComponent<[Renderer](Renderer.html)>();  
      
                    if (rend)
                        rend.sharedMaterial.color = matColor;
                }
            }  
      
            [EditorUtility.FocusProjectWindow](EditorUtility.FocusProjectWindow.html)();
        }  
      
        void OnInspectorUpdate()
        {
            Repaint();
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

