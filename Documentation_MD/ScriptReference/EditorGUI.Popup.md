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

#  [EditorGUI](EditorGUI.html).Popup

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

public static int Popup([Rect](Rect.html) position, int selectedIndex,
string[] displayedOptions, [GUIStyle](GUIStyle.html) style =
EditorStyles.popup);

## Declaration

public static int Popup([Rect](Rect.html) position, int selectedIndex,
GUIContent[] displayedOptions, [GUIStyle](GUIStyle.html) style =
EditorStyles.popup);

## Declaration

public static int Popup([Rect](Rect.html) position, string label, int
selectedIndex, string[] displayedOptions, [GUIStyle](GUIStyle.html) style =
EditorStyles.popup);

## Declaration

public static int Popup([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, int selectedIndex, GUIContent[]
displayedOptions, [GUIStyle](GUIStyle.html) style = EditorStyles.popup);

### Parameters

position | Rectangle on the screen to use for the field.  
---|---  
label | Optional label in front of the field.  
selectedIndex | The index of the option the field shows.  
displayedOptions | An array with the options shown in the popup.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**int** The index of the option that has been selected by the user.

### Description

Makes a generic popup selection field.

Takes the currently selected index as a parameter and returns the index
selected by the user.  
  
![](../StaticFiles/ScriptRefImages/EditorGUIPopup.png)  
_Popup in and Editor Window._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    
    // Adds a component to the selected GameObjects  
      
    class EditorGUIPopup : [EditorWindow](EditorWindow.html)
    {
        string[] options = { "[Rigidbody](Rigidbody.html)", "[Box](UIElements.Box.html) [Collider](Collider.html)", "Sphere [Collider](Collider.html)" };
        int index = 0;  
      
        [[MenuItem](MenuItem.html)("Examples/[Editor](Editor.html) [GUI](GUI.html) Popup usage")]
        static void Init()
        {
            var window = GetWindow<EditorGUIPopup>();
            window.position = new [Rect](Rect.html)(0, 0, 180, 80);
            window.Show();
        }  
      
        void OnGUI()
        {
            index = [EditorGUI.Popup](EditorGUI.Popup.html)(
                new [Rect](Rect.html)(0, 0, position.width, 20),
                "[Component](Component.html):",
                index,
                options);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 25, position.width, position.height - 26), "Add [Component](Component.html)"))
                AddComponentToObjects();
        }  
      
        void AddComponentToObjects()
        {
            if (![Selection.activeGameObject](Selection-activeGameObject.html))
            {
                [Debug.LogError](Debug.LogError.html)("Please select at least one [GameObject](GameObject.html) first");
                return;
            }  
      
            foreach ([GameObject](GameObject.html) obj in [Selection.gameObjects](Selection-gameObjects.html))
            {
                switch (index)
                {
                    case 0:
                        obj.AddComponent<[Rigidbody](Rigidbody.html)>();
                        break;  
      
                    case 1:
                        obj.AddComponent<[BoxCollider](BoxCollider.html)>();
                        break;  
      
                    case 2:
                        obj.AddComponent<[SphereCollider](SphereCollider.html)>();
                        break;
                }
            }
        }
    }
    

**Note:** The `displayedOptions` lists an array of options. When these
elements contain "/" (slash characters) the elements are use for sub-menus.
The text to the left of the slashes determines the structure.

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

