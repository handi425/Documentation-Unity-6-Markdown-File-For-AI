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

#
[IPopupMenuExtension](VersionControl.IPopupMenuExtension.html).DisplayPopupMenu

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

public void DisplayPopupMenu([Rect](Rect.html) position);

### Parameters

position | The position of the context menu.  
---|---  
  
### Description

Displays a version control system context menu.

The menu is shown when a user right clicks the top left corner of an asset
icon.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html), [IPopupMenuExtension](VersionControl.IPopupMenuExtension.html)
    {
        public void DisplayPopupMenu([Rect](Rect.html) position)
        {
            [EditorUtility.DisplayPopupMenu](EditorUtility.DisplayPopupMenu.html)(position, "CONTEXT/Custom", null);
        }  
      
        [[MenuItem](MenuItem.html)("CONTEXT/Custom/Print Selected Assets")]
        static void PrintSelectedAssets()
        {
            var guids = [Selection.assetGUIDs](Selection-assetGUIDs.html);
            if (guids == null || guids.Length == 0)
            {
                [Debug.LogWarning](Debug.LogWarning.html)("Empty selection.");
                return;
            }  
      
            var message = "Selected asset(s):";
            foreach (var guid in guids)
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                message += ' ' + path;
            }
            [Debug.Log](Debug.Log.html)(message);
        }
    }
    

Additional resources:
[IPopupMenuExtension](VersionControl.IPopupMenuExtension.html),
[VersionControlObject](VersionControl.VersionControlObject.html).

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

