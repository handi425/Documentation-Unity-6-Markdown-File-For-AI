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
[SerializationUtility](SerializationUtility.html).ClearAllManagedReferencesWithMissingTypes

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

public static bool
ClearAllManagedReferencesWithMissingTypes([Object](Object.html) obj);

### Description

Removes all managed references that are missing their type.

This method removes all serialized data associated with managed reference
fields that have missing types.  
  
This API is useful for removing missing type warning messages when an asset is
loaded, for example if there is a reference to a class in a package that is
not being used anymore.  
  
This method returns false if the object had no references with missing types.  
  
Additional resources:
[ClearManagedReferenceWithMissingType](SerializationUtility.ClearManagedReferenceWithMissingType.html),
[SerializeReference](SerializeReference.html).

    
    
    using System.Collections.Generic;
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ClearMissingTypeExample
    {
        [[MenuItem](MenuItem.html)("Example/Clear [ScriptableObject](ScriptableObject.html) References with Missing Types")]
        static public void ClearMissingTypesOnScriptableObjects()
        {
            var report = new StringBuilder();  
      
            var guids = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:[ScriptableObject](ScriptableObject.html)", new[] {"Assets"});
            foreach (string guid in guids)
            {
                var path = [AssetDatabase.GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)(guid);
                Object obj = [AssetDatabase.LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)(path);
                if (obj != null)
                {
                    if ([SerializationUtility.ClearAllManagedReferencesWithMissingTypes](SerializationUtility.ClearAllManagedReferencesWithMissingTypes.html)(obj))
                    {
                        report.Append("Cleared missing types from ").Append(path).AppendLine();
                    }
                    else
                    {
                        report.Append("No missing types to clear on ").Append(path).AppendLine();
                    }
                }
            }  
      
            [Debug.Log](Debug.Log.html)(report.ToString());
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

