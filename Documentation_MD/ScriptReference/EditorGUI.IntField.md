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

#  [EditorGUI](EditorGUI.html).IntField

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

public static int IntField([Rect](Rect.html) position, int value,
[GUIStyle](GUIStyle.html) style = EditorStyles.numberField);

## Declaration

public static int IntField([Rect](Rect.html) position, string label, int
value, [GUIStyle](GUIStyle.html) style = EditorStyles.numberField);

## Declaration

public static int IntField([Rect](Rect.html) position,
[GUIContent](GUIContent.html) label, int value, [GUIStyle](GUIStyle.html)
style = EditorStyles.numberField);

### Parameters

position | Rectangle on the screen to use for the int field.  
---|---  
label | Optional label to display in front of the int field.  
value | The value to edit.  
style | Optional [GUIStyle](GUIStyle.html).  
  
### Returns

**int** The value entered by the user.

### Description

Makes a text field for entering integers.

![](../StaticFiles/ScriptRefImages/EditorGUIIntField.png)  
_Int Field in an Editor Window._

    
    
    //Create a folder and name it "[Editor](Editor.html)" (Right click in your Project [Asset](VersionControl.Asset.html) folder and go to Create>[Folder](WSA.Folder.html)) if you don't already have one
    //Place this script in the [Editor](Editor.html) folder
    //This script creates a new menu at the top of the [Editor](Editor.html) named "Examples" with one item "Clone Object".  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class Example : [EditorWindow](EditorWindow.html)
    {
        int clones = 1;  
      
        [[MenuItem](MenuItem.html)("Examples/Clone Object")]
        static void Init()
        {
            //Create the new [Editor](Editor.html) window and show it
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(Example));
            window.Show();
        }  
      
        void OnGUI()
        {
            //The field which allows you to input the amount of clones of a [GameObject](GameObject.html) you want
            clones = [EditorGUI.IntField](EditorGUI.IntField.html)(new [Rect](Rect.html)(0, 35, position.width, 15), "Number of clones:", clones);  
      
            //If there isn't a currently selected [GameObject](GameObject.html), this message appears
            if ([Selection.activeGameObject](Selection-activeGameObject.html) == null)
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(3, 3, position.width, 20), "Please click on a [GameObject](GameObject.html) in your [Scene](SceneManagement.Scene.html)!");  
      
            //Press the clone [Button](UIElements.Button.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 55, position.width, 20), "Clone!"))
            {
                //Check that you have a [GameObject](GameObject.html) selected
                if ([Selection.activeGameObject](Selection-activeGameObject.html) != null)
                {
                    //Loop until the number of clones is reached
                    for (int i = 0; i < clones; i++)
                    {
                        //Spawn each of the clones
                        Instantiate([Selection.activeGameObject](Selection-activeGameObject.html), [Vector3.zero](Vector3-zero.html), [Quaternion.identity](Quaternion-identity.html));
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

