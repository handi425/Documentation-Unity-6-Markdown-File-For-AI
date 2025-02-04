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

#  [DropdownMenu](UIElements.DropdownMenu.html).RemoveItemAt

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

public void RemoveItemAt(int index);

### Parameters

index | The index of the item to remove.  
---|---  
  
### Description

Removes the menu item at index.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    public class ContextMenuWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("My/Context [Menu](Menu.html) Window")]
        static void ShowMe() => GetWindow<ContextMenuWindow>();  
      
        void CreateGUI()
        {
            var contextMenuContainer = new [VisualElement](UIElements.VisualElement.html)();
            contextMenuContainer.style.flexGrow = 1;
            contextMenuContainer.AddManipulator(new [ContextualMenuManipulator](UIElements.ContextualMenuManipulator.html)(e =>
            {
                e.menu.AppendAction("My [Action](Unity.Android.Gradle.Manifest.Action.html) 1", a => [Debug.Log](Debug.Log.html)("My [Action](Unity.Android.Gradle.Manifest.Action.html) 1 Works"), [DropdownMenuAction.Status.Normal](UIElements.DropdownMenuAction.Status.Normal.html));
                e.menu.AppendAction("My [Action](Unity.Android.Gradle.Manifest.Action.html) 2", a => [Debug.Log](Debug.Log.html)("My [Action](Unity.Android.Gradle.Manifest.Action.html) 2 Works"), [DropdownMenuAction.Status.Normal](UIElements.DropdownMenuAction.Status.Normal.html));
                e.menu.AppendAction("My [Action](Unity.Android.Gradle.Manifest.Action.html) 3", a => [Debug.Log](Debug.Log.html)("My [Action](Unity.Android.Gradle.Manifest.Action.html) 3 Works"), [DropdownMenuAction.Status.Normal](UIElements.DropdownMenuAction.Status.Normal.html));  
      
                e.menu.RemoveItemAt(0); // Remove My [Action](Unity.Android.Gradle.Manifest.Action.html) 1
                e.menu.RemoveItemAt(1); // Remove My [Action](Unity.Android.Gradle.Manifest.Action.html) 3 (item indices have shifted after first removal)
            }));  
      
            rootVisualElement.Add(contextMenuContainer);
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

