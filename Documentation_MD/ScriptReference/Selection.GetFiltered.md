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

#  [Selection](Selection.html).GetFiltered

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

public static Object[] GetFiltered(Type type,
[SelectionMode](SelectionMode.html) mode);

### Parameters

type | Only objects of this type will be retrieved.  
---|---  
mode | Further options to refine the selection.  
  
### Description

Returns the current selection filtered by type and mode.

For a selected GameObject that has multiple Components of `type`, only the
first one will be included in the results.  
If `type` is a subclass of [Component](Component.html) or
[GameObject](GameObject.html) the full SelectionMode is supported.  
If `type` does not subclass from [Component](Component.html) or
[GameObject](GameObject.html) (eg. [Mesh](Mesh.html) or
[ScriptableObject](ScriptableObject.html)) only
[SelectionMode.ExcludePrefab](SelectionMode.ExcludePrefab.html) and
[SelectionMode.Editable](SelectionMode.Editable.html) are supported.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class ToggleActive : [ScriptableObject](ScriptableObject.html)
    {
        [[MenuItem](MenuItem.html)("Example/[Toggle](UIElements.Toggle.html) Active of Selected %i")]
        static void DoToggle()
        {
            Object[] activeGOs =
                [Selection.GetFiltered](Selection.GetFiltered.html)(
                    typeof([GameObject](GameObject.html)),
                    [SelectionMode.Editable](SelectionMode.Editable.html) | [SelectionMode.TopLevel](SelectionMode.TopLevel.html));  
      
            foreach ([GameObject](GameObject.html) obj in activeGOs)
            {
                obj.SetActive(!obj.activeSelf);
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

