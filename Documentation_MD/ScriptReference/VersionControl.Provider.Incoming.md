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

#  [Provider](VersionControl.Provider.html).Incoming

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

public static [VersionControl.Task](VersionControl.Task.html) Incoming();

### Description

Starts a task that queries the version control server for incoming changes.

The task returns the incoming changesets which then can be accessed through
the task's [Task.changeSets](VersionControl.Task-changeSets.html) property
once it has been completed.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/Incoming")]
        public static void ExampleIncoming()
        {
            [ChangeSets](VersionControl.ChangeSets.html) exampleChangesets = new [ChangeSets](VersionControl.ChangeSets.html)();
            [ChangeSet](VersionControl.ChangeSet.html) exampleChangeset = new [ChangeSet](VersionControl.ChangeSet.html)();
            [Task](VersionControl.Task.html) t1 = [Provider.Incoming](VersionControl.Provider.Incoming.html)();
            t1.Wait();
            exampleChangesets = t1.changeSets;
            exampleChangeset = exampleChangesets[0];
            [Task](VersionControl.Task.html) t2 = [Provider.IncomingChangeSetAssets](VersionControl.Provider.IncomingChangeSetAssets.html)(exampleChangeset);
            t2.Wait();
            t2.assetList.ForEach(asset => [Debug.Log](Debug.Log.html)(asset.name + " " + asset.state.ToString()));
        }
    }
    

The code above fetches the incoming changesets using
[Provider.Incoming](VersionControl.Provider.Incoming.html) and parses it to
[Provider.IncomingChangeSetAssets](VersionControl.Provider.IncomingChangeSetAssets.html)
in order to output the incoming asset file names and their status.

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

