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

#  [Undo](Undo.html).RegisterChildrenOrderUndo

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

public static void RegisterChildrenOrderUndo([Object](Object.html)
objectToUndo, string name);

### Parameters

objectToUndo | The object whose child order should be recorded on the undo stack.  
---|---  
name | The name of the undo operation.  
  
### Description

Stores a copy of the order of the object's children on the undo stack.

If the undo is performed, the order of the object's children will be restored
to the recorded state.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class UndoExamples
    {
        [[MenuItem](MenuItem.html)("[Undo](Undo.html) Examples/RegisterChildrenOrderUndo")]
        static void Example()
        {
            var parent = new [GameObject](GameObject.html)("Parent");
            for (int childIndex = 0; childIndex < 5; childIndex += 1)
            {
                var child = new [GameObject](GameObject.html)($"Child{childIndex}");
                child.transform.parent = parent.transform;
            }  
      
            // Store the states of the parent object.
            [Undo.RegisterChildrenOrderUndo](Undo.RegisterChildrenOrderUndo.html)(parent.transform, "Set as last sibling");
            parent.transform.GetChild(0).SetAsLastSibling();  
      
            // If you choose "Edit->[Undo](Undo.html) Set as last sibling" from the main menu now, the order of the children will be restored.
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

