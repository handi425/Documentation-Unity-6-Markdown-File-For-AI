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

# Provider

class in UnityEditor.VersionControl

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

This class provides access to the version control API.

Note that the Version Control window is refreshed after every version control
operation. This means that looping through multiple assets and doing an
individual operation on each (i.e. Checkout) will be slower than passing an
[AssetList](VersionControl.AssetList.html) containing all of the assets and
performing a version control operation on it once.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("VC/Checkout")]
        public static void TestCheckout()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add(new [Asset](VersionControl.Asset.html)("Assets/"));  
      
            [Task](VersionControl.Task.html) t = [Provider.Checkout](VersionControl.Provider.Checkout.html)(assets, [CheckoutMode.Both](VersionControl.CheckoutMode.Both.html));
            t.Wait();
        }
    }
    

Also note that Provider operations just execute the VCS commands, and do not
automatically refresh the Version Control window. To update this window, use
[Task.SetCompletionAction](VersionControl.Task.SetCompletionAction.html).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("VC/ChangeSetMove")]
        static void ChangeSetMove()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/testMaterial.mat"));
            [Task](VersionControl.Task.html) task = [Provider.ChangeSetMove](VersionControl.Provider.ChangeSetMove.html)(assets, "ChangeSetID");
            task.SetCompletionAction([CompletionAction.UpdatePendingWindow](VersionControl.CompletionAction.UpdatePendingWindow.html));
        }
    }
    

### Static Properties

[activeTask](VersionControl.Provider-activeTask.html)| Gets the currently
executing task.  
---|---  
[enabled](VersionControl.Provider-enabled.html)| Returns true if the version
control provider is enabled and a valid Unity Pro License was found.  
[hasCheckoutSupport](VersionControl.Provider-hasCheckoutSupport.html)| This is
true if the currently selected version control plugin supports the Checkout
method.  
[hasLockingSupport](VersionControl.Provider-hasLockingSupport.html)| This is
true if the currently selected version control plugin supports the Lock and
Unlock methods.  
[isActive](VersionControl.Provider-isActive.html)| Returns true if a version
control plugin has been selected and configured correctly.  
[offlineReason](VersionControl.Provider-offlineReason.html)| Returns the
reason for the version control provider being offline (if it is offline).  
[onlineState](VersionControl.Provider-onlineState.html)| Returns the
OnlineState of the version control provider.  
[preCheckoutCallback](VersionControl.Provider-preCheckoutCallback.html)| User-
supplied callback to be called before Version Control check out operation.  
[preSubmitCallback](VersionControl.Provider-preSubmitCallback.html)| User-
supplied callback to be called before Version Control Submit operation.  
[requiresNetwork](VersionControl.Provider-requiresNetwork.html)| This is true
if a network connection is required by the currently selected version control
plugin to perform any action.  
  
### Static Methods

[Add](VersionControl.Provider.Add.html)| Allows you to add files to version
control via script.  
---|---  
[AddIsValid](VersionControl.Provider.AddIsValid.html)| Given a list of assets
this function returns true if Provider.Add is a valid task to perform on at
least one of the assets in the list.  
[ChangeSetDescription](VersionControl.Provider.ChangeSetDescription.html)|
Given a changeset only containing the changeset ID, this will start a task for
quering the description of the changeset.  
[ChangeSetMove](VersionControl.Provider.ChangeSetMove.html)| Move an Asset or
a list of Assets from their current changeset to a new changeset.  
[ChangeSets](VersionControl.Provider.ChangeSets.html)| Gets a list of pending
changesets owned by the current user.  
[ChangeSetStatus](VersionControl.Provider.ChangeSetStatus.html)| Retrieves a
list of assets belonging to a changeset.  
[Checkout](VersionControl.Provider.Checkout.html)| Checkout an asset or a list
of assets from the version control system.  
[CheckoutIsValid](VersionControl.Provider.CheckoutIsValid.html)| Given an
asset or a list of assets this function returns true if Provider.Checkout is a
valid task to perform on at least one of the given assets.  
[ClearCache](VersionControl.Provider.ClearCache.html)| This will invalidate
the cached state information for all assets.  
[Delete](VersionControl.Provider.Delete.html)| Starts a task to delete an
Asset or a list of Assets from the disk and from the version control system.  
[DeleteChangeSets](VersionControl.Provider.DeleteChangeSets.html)| Starts a
task that will attempt to delete the given changesets.  
[DeleteChangeSetsIsValid](VersionControl.Provider.DeleteChangeSetsIsValid.html)|
Tests if deleting the given changesets is a valid task to perform.  
[DiffHead](VersionControl.Provider.DiffHead.html)| Starts a task for showing a
diff of the given assest versus their head revision.  
[DiffIsValid](VersionControl.Provider.DiffIsValid.html)| Returns true if
starting a Diff task is a valid operation for at least one asset in the given
AssetList.  
[GetActiveConfigFields](VersionControl.Provider.GetActiveConfigFields.html)|
Returns the configuration fields for the currently active version control
plugin.  
[GetActivePlugin](VersionControl.Provider.GetActivePlugin.html)| Gets the
current, user selected verson control Plugin.  
[GetAssetByGUID](VersionControl.Provider.GetAssetByGUID.html)| Returns version
control information about an asset from a given GUID.  
[GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)| Returns the
version control information about an asset. Can be used with "AssetList.Add"
to add assets to a list for further version control actions.  
[GetAssetListFromSelection](VersionControl.Provider.GetAssetListFromSelection.html)|
Returns the version control information about the currently selected Assets.  
[GetLatest](VersionControl.Provider.GetLatest.html)| Start a task for getting
the latest version of an out of sync asset from the version control server.  
[GetLatestIsValid](VersionControl.Provider.GetLatestIsValid.html)| The task
tests the given asset list and returns true if Provider.GetLatest is valid
operation for one or more assets.  
[Incoming](VersionControl.Provider.Incoming.html)| Starts a task that queries
the version control server for incoming changes.  
[IncomingChangeSetAssets](VersionControl.Provider.IncomingChangeSetAssets.html)|
Given an incoming changeset this will start a task to query the version
control server for which assets are part of the changeset.  
[IsOpenForEdit](VersionControl.Provider.IsOpenForEdit.html)| Returns true if
an asset can be edited.  
[Lock](VersionControl.Provider.Lock.html)| Attempt to lock an asset for
exclusive editing.  
[LockIsValid](VersionControl.Provider.LockIsValid.html)| Returns true if the
Provider.Lock task can be executed on one or more assets from the given asset
list.  
[Merge](VersionControl.Provider.Merge.html)| Initiates a merge task to handle
the merging of conflicting Assets. This invokes a merge tool, which you can
set in the External Tools section of the Preferences window, on the
conflicting Assets. When the merge task finishes, the AssetList only contains
the Assets that the tool could merge.  
[Move](VersionControl.Provider.Move.html)| Uses the version control plugin to
move an asset from one path to another.  
[Resolve](VersionControl.Provider.Resolve.html)| Starts a task that will
resolve the conflicting assets in version control.  
[ResolveIsValid](VersionControl.Provider.ResolveIsValid.html)| Tests if any of
the assets in the list have the conflicted state and can be resolved.  
[Revert](VersionControl.Provider.Revert.html)| Reverts the specified assets by
undoing any changes done since the last time you synced.  
[RevertIsValid](VersionControl.Provider.RevertIsValid.html)| Returns true if
Provider.Revert is a valid task to perform on at least one of the given assets
in the list.  
[Status](VersionControl.Provider.Status.html)| Starts a task that will fetch
the most recent status about the asset or assets from the revision control
system.  
[Submit](VersionControl.Provider.Submit.html)| Starts a task that submits the
assets to version control.  
[SubmitIsValid](VersionControl.Provider.SubmitIsValid.html)| Returns true if
submitting the assets is a valid operation.  
[UnlockIsValid](VersionControl.Provider.UnlockIsValid.html)| Returns true if
unlocking the assets is a valid operation.  
[UpdateSettings](VersionControl.Provider.UpdateSettings.html)| Starts a task
that sends the version control settings to the version control system.  
  
### Delegates

[PreCheckoutCallback](VersionControl.Provider.PreCheckoutCallback.html)|
Delegate for a user-supplied callback to be called before Version Control
Checkout.  
---|---  
[PreSubmitCallback](VersionControl.Provider.PreSubmitCallback.html)| Delegate
for a user-supplied callback to be called before Version Control Submit.  
  
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

