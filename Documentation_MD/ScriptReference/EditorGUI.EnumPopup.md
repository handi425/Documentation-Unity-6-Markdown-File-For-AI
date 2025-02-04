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

#  [EditorGUI](EditorGUI.html).EnumPopup

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

public static Enum EnumPopup([Rect](Rect.html) position, Enum selected,
[GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static Enum EnumPopup([Rect](Rect.html) position, string label, Enum
selected, [GUIStyle](GUIStyle.html) style = EditorStyles.popup);

## Declaration

public static Enum EnumPopup([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, Enum selected, [GUIStyle](GUIStyle.html)
style = EditorStyles.popup);

## Declaration

public static Enum EnumPopup([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, Enum selected, Func<Enum,bool>
checkEnabled = null, bool includeObsolete = false, [GUIStyle](GUIStyle.html)
style = null);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label in front of the field.  
selected | The enum option the field shows.  
style | Optional [GUIStyle](GUIStyle.html).  
includeObsolete | Set to true to include Enum values with ObsoleteAttribute. Set to false to exclude Enum values with ObsoleteAttribute.  
checkEnabled | Method called for each Enum value displayed. The specified method should return true if the option can be selected, false otherwise.  
  
### Returns

**Enum** The enum option that has been selected by the user.

### Description

Makes an enum popup selection field.

Takes the currently selected enum value as a parameter and returns the enum
value selected by the user.
![](../StaticFiles/ScriptRefImages/EditorGUIEnumPopup.png)  
_Enum Popup in an Editor Window._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    
    // Shows info of a [GameObject](GameObject.html) depending on the selected option  
      
    public enum OPTIONS
    {
        [Position](UIElements.Position.html) = 0,
        Rotation = 1,
        [Scale](UIElements.Scale.html) = 2,
    }  
      
    
    public class EditorGUIEnumPopup : [EditorWindow](EditorWindow.html)
    {
        OPTIONS display = OPTIONS.Position;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUI](GUI.html) Enum Popup usage")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUIEnumPopup));
            window.position = new [Rect](Rect.html)(0, 0, 220, 80);
            window.Show();
        }  
      
        void OnGUI()
        {
            [Transform](Transform.html) selectedObj = [Selection.activeTransform](Selection-activeTransform.html);  
      
            display = (OPTIONS)[EditorGUI.EnumPopup](EditorGUI.EnumPopup.html)(
                new [Rect](Rect.html)(3, 3, position.width - 6, 15),
                "Show:",
                display);  
      
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(0, 20, position.width, 15),
                "Name:",
                selectedObj ? selectedObj.name : "Select an Object");
            if (selectedObj)
            {
                switch (display)
                {
                    case OPTIONS.Position:
                        [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(0, 40, position.width, 15),
                            "[Position](UIElements.Position.html):",
                            selectedObj.position.ToString());
                        break;  
      
                    case OPTIONS.Rotation:
                        [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(0, 40, position.width, 15),
                            "Rotation:",
                            selectedObj.rotation.ToString());
                        break;  
      
                    case OPTIONS.Scale:
                        [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(0, 40, position.width, 15),
                            "[Scale](UIElements.Scale.html):",
                            selectedObj.localScale.ToString());
                        break;  
      
                    default:
                        [Debug.LogError](Debug.LogError.html)("Unrecognized Option");
                        break;
                }
            }  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(3, position.height - 25, position.width - 6, 24), "Close"))
                this.Close();
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

