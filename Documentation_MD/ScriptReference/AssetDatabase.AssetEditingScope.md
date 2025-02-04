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

# AssetEditingScope

class in UnityEditor

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

Places the Asset Database into a state that temporarily prevents automatic
import, allowing you to group several asset imports together into one larger
import.

This class allows you to pause the Asset Database's automatic import of new or
modified assets. This is useful if you want to perform actions via script that
make multiple changes to assets without the Asset Database importing each
change in a separate import process.  
  
Instead, you can pause imports, make multiple changes, then resume imports,
which means Unity will only perform one input process for all the changes you
made while the importing was paused.  
  
This class is an alternative to the
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html) and
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html) methods,
which serve the same purpose.  
  
The `AssetEditingScope` class is intended to be used within a `using`
statement, which automatically disposes of the class, as in the following
example:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetEditingScopeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/[AssetEditingScope](AssetDatabase.AssetEditingScope.html)")]
        static void CallAssetDatabaseAPIsBetweenAssetEditingScope()
        {
            // Place the [Asset](VersionControl.Asset.html) Database in a state where
            // importing is suspended for most APIs
            using (var editingScope = new [AssetDatabase.AssetEditingScope](AssetDatabase.AssetEditingScope.html)())
            {
                // Modify the assets however we like
                [AssetDatabase.CopyAsset](AssetDatabase.CopyAsset.html)("Assets/CopyAsset.txt", "Assets/Text/CopyAsset.txt");
                [AssetDatabase.MoveAsset](AssetDatabase.MoveAsset.html)("Assets/MoveAsset.txt", "Assets/Text/MoveAsset.txt");
            }
            // Assets will now be imported again, as editingScope has been disposed.
        }
    }
    

If you use it in a different context other than a `using` statement, you must
ensure that its `Dispose()` method is called or the Asset Database will remain
in a paused state.  
  
Additional resources:
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html),
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html).

### Constructors

[AssetDatabase.AssetEditingScope](AssetDatabase.AssetEditingScope-ctor.html)|
Instantiates AssetEditingScope. Equivalent to calling
AssetDatabase.StartAssetEditing().  
---|---  
  
### Public Methods

[Dispose](AssetDatabase.AssetEditingScope.Dispose.html)| Disposes of
AssetEditingScope. Equivalent to calling AssetDatabase.StopAssetEditing().  
---|---  
  
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

