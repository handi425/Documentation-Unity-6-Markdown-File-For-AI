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

#  [EditorWindow](EditorWindow.html).ShowUtility

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

public void ShowUtility();

### Description

Show the EditorWindow as a floating utility window.

When the utility window loses focus it remains on top of the new active
window. This means the
[EditorWindow.ShowUtility](EditorWindow.ShowUtility.html) window is never
hidden by the Unity editor. It is, however, not dockable to the editor.  
  
Utility windows will always be in front of normal Unity windows. It will be
hidden when the user switches from Unity to another application.  
  
**Note:** You do not need to use
[EditorWindow.GetWindow](EditorWindow.GetWindow.html) before using this
function to show the window.

    
    
    // Simple script that randomizes the rotation of the selected GameObjects.
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;
    
    public class RandomizeInSelectionShowUtility : [EditorWindow](EditorWindow.html)
    {
        System.Random random = new System.Random();
        public float rotationAmount;
        public string selected = "";
    
        [[MenuItem](MenuItem.html)("Examples/Randomize Objects")]
        static void Init()
        {
            RandomizeInSelectionShowUtility window =
                [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<RandomizeInSelectionShowUtility>(true, "Randomize Objects");
            window.ShowUtility();
        }
    
        void CreateGUI()
        {
            var label = new [Label](UIElements.Label.html)("Selected an object and click Randomize!");
            rootVisualElement.Add(label);
    
            var buttonRandomize = new [Button](UIElements.Button.html)();
            buttonRandomize.text = "Randomize!";
            buttonRandomize.clicked += () => RandomizeSelected();
            rootVisualElement.Add(buttonRandomize);
        }
    
        void RandomizeSelected()
        {
            foreach (var transform in [Selection.transforms](Selection-transforms.html))
            {
                [Quaternion](Quaternion.html) rotation = [Random.rotation](Random-rotation.html);
                rotationAmount = (float)random.NextDouble();
                transform.localRotation = [Quaternion.Slerp](Quaternion.Slerp.html)(transform.localRotation, rotation, rotationAmount);
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

