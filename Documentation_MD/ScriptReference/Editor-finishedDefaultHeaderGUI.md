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

#  [Editor](Editor.html).finishedDefaultHeaderGUI

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

An event raised while drawing the header of the Inspector window, after the
default header items have been drawn.

Add an event handler to this event in order to draw additional items in the
header for the [Editor](Editor.html) passed to the event handler method.  
  
The following example script displays an asset's GUID as a copyable label in
the header, if the inspected object is a persistent asset and not a Scene
object. Copy this example script into a file called EditorHeaderGUID.cs and
put it in a folder called Editor.  
  
![](../StaticFiles/ScriptRefImages/FinishedDefaultHeaderGUI.png) _The
Inspector header with a custom GUID control added._

    
    
    using [UnityEditor](UnityEditor.html);  
      
    [[InitializeOnLoadAttribute](InitializeOnLoadAttribute.html)]
    static class EditorHeaderGUID
    {
        static EditorHeaderGUID()
        {
            [Editor.finishedDefaultHeaderGUI](Editor-finishedDefaultHeaderGUI.html) += DisplayGUIDIfPersistent;
        }  
      
        static void DisplayGUIDIfPersistent([Editor](Editor.html) editor)
        {
            if (![EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)(editor.target))
                return;  
      
            var guid = [AssetDatabase.AssetPathToGUID](AssetDatabase.AssetPathToGUID.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(editor.target));
            var totalRect = [EditorGUILayout.GetControlRect](EditorGUILayout.GetControlRect.html)();
            var controlRect = [EditorGUI.PrefixLabel](EditorGUI.PrefixLabel.html)(totalRect, EditorGUIUtility.TrTempContent("GUID"));
            if (editor.targets.Length > 1)
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(controlRect, EditorGUIUtility.TrTempContent("[Multiple objects selected]"));
            else
                [EditorGUI.SelectableLabel](EditorGUI.SelectableLabel.html)(controlRect, guid);
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

