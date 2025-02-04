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

#  [EditorGUI](EditorGUI.html).ColorField

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

public static [Color](Color.html) ColorField([Rect](Rect.html) position,
[Color](Color.html) value);

## Declaration

public static [Color](Color.html) ColorField([Rect](Rect.html) position,
string label, [Color](Color.html) value);

## Declaration

public static [Color](Color.html) ColorField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Color](Color.html) value);

## Declaration

public static [Color](Color.html) ColorField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Color](Color.html) value, bool
showEyedropper, bool showAlpha, bool hdr);

**Obsolete** Use EditorGUI.ColorField(Rect position, GUIContent label, Color
value, bool showEyedropper, bool showAlpha, bool hdr).

## Declaration

public static [Color](Color.html) ColorField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, [Color](Color.html) value, bool
showEyedropper, bool showAlpha, bool hdr,
[ColorPickerHDRConfig](ColorPickerHDRConfig.html) hdrConfig);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label to display in front of the field.  
value | The color to edit.  
showEyedropper | If true, the color picker should show the eyedropper control. If false, don't show it.  
showAlpha | If true, allow the user to set an alpha value for the color. If false, hide the alpha component.  
hdr | If true, treat the color as an HDR value. If false, treat it as a standard LDR value.  
  
### Returns

**Color** The color selected by the user.

### Description

Makes a field for selecting a [Color](Color.html).

![](../StaticFiles/ScriptRefImages/EditorGUIColorField.png)  
_Color field in an Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Change The color of the selected Game Objects
    class EditorGUIColorField : [EditorWindow](EditorWindow.html)
    {
        [Color](Color.html) matColor  = [Color.white](Color-white.html);  
      
        [[MenuItem](MenuItem.html)("Examples/Mass [Color](Color.html) Change")]  
      
        static void Init()
        {
            var window = GetWindow<EditorGUIColorField>();
            window.position = new [Rect](Rect.html)(0, 0, 170, 60);
            window.Show();
        }  
      
        void OnGUI()
        {
            matColor = [EditorGUI.ColorField](EditorGUI.ColorField.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 15),
                "New [Color](Color.html):",
                matColor);
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 30), "Change!"))
            {
                ChangeColors();
            }
        }  
      
        void ChangeColors()
        {
            if ([Selection.activeGameObject](Selection-activeGameObject.html))
            {
                foreach ([GameObject](GameObject.html) obj in [Selection.gameObjects](Selection-gameObjects.html))
                {
                    [Renderer](Renderer.html) rend = obj.GetComponent<[Renderer](Renderer.html)>();  
      
                    if (rend != null)
                    {
                        rend.sharedMaterial.color = matColor;
                    }
                }
            }
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

