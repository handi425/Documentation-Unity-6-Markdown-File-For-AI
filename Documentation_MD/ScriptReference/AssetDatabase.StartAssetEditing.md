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

#  [AssetDatabase](AssetDatabase.html).StartAssetEditing

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

public static void StartAssetEditing();

### Description

Places the Asset Database into a state that temporarily prevents automatic
import, allowing you to group several asset imports together into one larger
import.

This method allows you to pause the Asset Database's automatic import of new
or modified assets. This is useful if you want to perform actions via script
that make multiple changes to assets without the Asset Database importing each
change in a separate import process.  
  
Instead, you can pause imports, make multiple changes, then resume imports,
which means Unity will only perform one input process for all the changes you
made while the importing was paused, as demonstrated in this example:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class StartStopAssetEditingExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("APIExamples/StartStopAssetEditing")]
        static void CallAssetDatabaseAPIsBetweenStartStopAssetEditing()
        {
            try
            {
                //Place the [Asset](VersionControl.Asset.html) Database in a state where
                //importing is suspended for most APIs
                [AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html)();  
      
                [AssetDatabase.CopyAsset](AssetDatabase.CopyAsset.html)("Assets/CopyAsset.txt", "Assets/Text/CopyAsset.txt");
                [AssetDatabase.MoveAsset](AssetDatabase.MoveAsset.html)("Assets/MoveAsset.txt", "Assets/Text/MoveAsset.txt");
            }
            finally
            {
                //By adding a call to StopAssetEditing inside
                //a "finally" block, we ensure the [AssetDatabase](AssetDatabase.html)
                //state will be reset when leaving this function
                [AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html)();
            }
        }
    }
    

Note: [AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html)
places the Asset Database in a state that prevents imports until
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html) is
called. This means that if an exception occurs between the two function calls,
the AssetDatabase will be unresponsive. For this reason, you should always
place calls to
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html) and
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html) inside
either a `try..catch block`, or a `try..finally` block as needed.  
  
Also note: In the paused state between
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html) and
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html), some
AssetDatabase APIs won't work as expected. This is because assets created
during the paused state are not fully created in the asset database before the
call to StopAssetEditing. As a rule of thumb you should postpone the use of
more involved AssetDatabase APIs until after the
[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html) call and
reserve the
[AssetDatabase.StartAssetEditing](AssetDatabase.StartAssetEditing.html)/[AssetDatabase.StopAssetEditing](AssetDatabase.StopAssetEditing.html)
scope for operations that do not require the assets involved to be fully
imported.  
  
A similar alternative way of pausing and resuming asset database imports is
available, by using the
[AssetDatabase.AssetEditingScope](AssetDatabase.AssetEditingScope.html) class
in a `using` statement.

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

