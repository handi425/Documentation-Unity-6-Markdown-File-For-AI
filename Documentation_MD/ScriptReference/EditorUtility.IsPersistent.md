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

#  [EditorUtility](EditorUtility.html).IsPersistent

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

public static bool IsPersistent([Object](Object.html) target);

### Description

Determines if an object is stored on disk.

Typically assets like Prefabs, textures, audio clips, animation clips,
materials are stored on disk.  
  
Returns false if the object lives in the Scene. Typically this is a game
object or component but it could also be a material that was created from code
and not stored in an asset but instead stored in the Scene.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    
    // Tells if an Object is stored on disk or not.
    public class PersistentInfo : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/Object on Disk?")]
        static void CheckPersistent()
        {
            bool persistent = [EditorUtility.IsPersistent](EditorUtility.IsPersistent.html)([Selection.activeObject](Selection-activeObject.html));
            [Debug.Log](Debug.Log.html)(Selection.activeObject.name + ": " + (persistent ? "Stored on disk" : "Not on disk"));
        }  
      
        [[MenuItem](MenuItem.html)("Examples/Object on Disk?", true)]
        static bool ValidateCheckPersistent()
        {
            return [Selection.activeObject](Selection-activeObject.html) != null;
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

