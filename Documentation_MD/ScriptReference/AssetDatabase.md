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

# AssetDatabase

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

An Interface for accessing assets and performing operations on assets.

### Static Properties

[ActiveRefreshImportMode](AssetDatabase.ActiveRefreshImportMode.html)| Gets
the refresh import mode currently in use by the asset database.  
---|---  
[DesiredWorkerCount](AssetDatabase.DesiredWorkerCount.html)| The desired
number of processes to use when importing assets, during an asset database
refresh.  
[GlobalArtifactDependencyVersion](AssetDatabase.GlobalArtifactDependencyVersion.html)|
Changes during Refresh if anything has changed that can invalidate any
artifact.  
[GlobalArtifactProcessedVersion](AssetDatabase.GlobalArtifactProcessedVersion.html)|
Changes whenever a new artifact is added to the artifact database.  
[onImportPackageItemsCompleted](AssetDatabase-
onImportPackageItemsCompleted.html)| Callback raised whenever a package import
successfully completes that lists the items selected to be imported.  
  
### Static Methods

[AddObjectToAsset](AssetDatabase.AddObjectToAsset.html)| Adds objectToAdd to
an existing asset at path.  
---|---  
[AllowAutoRefresh](AssetDatabase.AllowAutoRefresh.html)| Decrements an
internal counter which Unity uses to determine whether to allow automatic
AssetDatabase refreshing behavior.  
[AssetPathExists](AssetDatabase.AssetPathExists.html)| Check whether an asset
exists at the given path in the database.  
[AssetPathToGUID](AssetDatabase.AssetPathToGUID.html)| Get the GUID for the
asset at path.  
[CanConnectToCacheServer](AssetDatabase.CanConnectToCacheServer.html)| Checks
the availability of the Cache Server.  
[CanOpenAssetInEditor](AssetDatabase.CanOpenAssetInEditor.html)| Checks if
Unity can open an asset in the Editor.  
[CanOpenForEdit](AssetDatabase.CanOpenForEdit.html)| Query whether an Asset
file can be opened for editing in version control and is not exclusively
locked by another user or otherwise unavailable.  
[ClearImporterOverride](AssetDatabase.ClearImporterOverride.html)| Clears the
importer override for the asset.  
[ClearLabels](AssetDatabase.ClearLabels.html)| Removes all labels attached to
an asset.  
[CloseCacheServerConnection](AssetDatabase.CloseCacheServerConnection.html)|
Closes an active cache server connection. If no connection is active, then it
does nothing.  
[Contains](AssetDatabase.Contains.html)| Is object an asset?  
[CopyAsset](AssetDatabase.CopyAsset.html)| Duplicates the asset at path and
stores it at newPath.  
[CopyAssets](AssetDatabase.CopyAssets.html)| Duplicates assets in paths and
stores them in newPaths.  
[CreateAsset](AssetDatabase.CreateAsset.html)| Creates a new native Unity
asset.  
[CreateFolder](AssetDatabase.CreateFolder.html)| Creates a new folder, in the
specified parent folder.The parent folder string must start with the "Assets"
folder, and all folders within the parent folder string must already exist.
For example, when specifying "Assets/ParentFolder1/Parentfolder2/", the new
folder will be created in "ParentFolder2" only if ParentFolder1 and
ParentFolder2 already exist.  
[DeleteAsset](AssetDatabase.DeleteAsset.html)| Deletes the specified asset or
folder.  
[DeleteAssets](AssetDatabase.DeleteAssets.html)| Lets you delete multiple
assets or folders at once with performance benefits under version control.  
[DisallowAutoRefresh](AssetDatabase.DisallowAutoRefresh.html)| Increments an
internal counter which Unity uses to determine whether to allow automatic
AssetDatabase refreshing behavior.  
[ExportPackage](AssetDatabase.ExportPackage.html)| Exports the assets
identified by assetPathNames to a unitypackage file in fileName.  
[ExtractAsset](AssetDatabase.ExtractAsset.html)| Creates an external Asset
from an object (such as a Material) by extracting it from within an imported
asset (such as an FBX file).  
[FindAssets](AssetDatabase.FindAssets.html)| Search the asset database using
the search filter string.  
[ForceReserializeAssets](AssetDatabase.ForceReserializeAssets.html)| Forcibly
load and re-serialize the given assets, flushing any outstanding data changes
to disk.  
[ForceToDesiredWorkerCount](AssetDatabase.ForceToDesiredWorkerCount.html)|
Forces the Editor to use the desired amount of worker processes. Unity will
either spawn new worker processes or shut down idle worker processes to reach
the desired number.  
[GenerateUniqueAssetPath](AssetDatabase.GenerateUniqueAssetPath.html)| Creates
a new unique path for an asset.  
[GetAllAssetBundleNames](AssetDatabase.GetAllAssetBundleNames.html)| Return
all the AssetBundle names in the asset database.  
[GetAssetBundleDependencies](AssetDatabase.GetAssetBundleDependencies.html)|
Given an assetBundleName, returns the list of AssetBundles that it depends on.  
[GetAssetDependencyHash](AssetDatabase.GetAssetDependencyHash.html)| Returns
the hash of all the dependencies of an asset.  
[GetAssetOrScenePath](AssetDatabase.GetAssetOrScenePath.html)| Returns the
path name relative to the project folder where the asset is stored.  
[GetAssetPath](AssetDatabase.GetAssetPath.html)| Returns the path name
relative to the project folder where the asset is stored.  
[GetAssetPathFromTextMetaFilePath](AssetDatabase.GetAssetPathFromTextMetaFilePath.html)|
Gets the path to the asset file associated with a text .meta file.  
[GetAssetPathsFromAssetBundle](AssetDatabase.GetAssetPathsFromAssetBundle.html)|
Returns an array containing the paths of all assets marked with the specified
Asset Bundle name.  
[GetAssetPathsFromAssetBundleAndAssetName](AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName.html)|
Get the Asset paths for all Assets tagged with assetBundleName and named
assetName.  
[GetAvailableImporters](AssetDatabase.GetAvailableImporters.html)| Gets the
importer types associated with a given Asset path.  
[GetCachedIcon](AssetDatabase.GetCachedIcon.html)| Retrieves an icon for the
asset at the given asset path.  
[GetCacheServerAddress](AssetDatabase.GetCacheServerAddress.html)| Gets the IP
address of the Cache Server in Editor Settings.  
[GetCacheServerEnableDownload](AssetDatabase.GetCacheServerEnableDownload.html)|
Gets the Cache Server Download option from Editor Settings.  
[GetCacheServerEnableUpload](AssetDatabase.GetCacheServerEnableUpload.html)|
Gets the Cache Server Upload option from Editor Settings.  
[GetCacheServerNamespacePrefix](AssetDatabase.GetCacheServerNamespacePrefix.html)|
Gets the Cache Server Namespace prefix set in Editor Settings.  
[GetCacheServerPort](AssetDatabase.GetCacheServerPort.html)| Gets the Port
number of the Cache Server in Editor Settings.  
[GetCurrentCacheServerIp](AssetDatabase.GetCurrentCacheServerIp.html)| Gets
the IP address of the Cache Server currently in use by the Editor.  
[GetDefaultImporter](AssetDatabase.GetDefaultImporter.html)| Returns the
Default Importer associated with the asset located at the supplied path. When
no Importer override is set, then the default importer is used. Additional
resources: AssetDatabase.GetImporterOverride,
AssetDatabase.ClearImporterOverride.  
[GetDependencies](AssetDatabase.GetDependencies.html)| Returns an array of all
the assets that are dependencies of the asset at the specified pathName.Note:
GetDependencies() gets the Assets that are referenced by other Assets. For
example, a Scene could contain many GameObjects with a Material attached to
them. In this case, GetDependencies() will return the path to the Material
Assets, but not the GameObjects as those are not Assets on your disk.  
[GetImplicitAssetBundleName](AssetDatabase.GetImplicitAssetBundleName.html)|
Returns the name of the AssetBundle that a given asset belongs to.  
[GetImplicitAssetBundleVariantName](AssetDatabase.GetImplicitAssetBundleVariantName.html)|
Returns the name of the AssetBundle Variant that a given asset belongs to.  
[GetImporterOverride](AssetDatabase.GetImporterOverride.html)| Returns the
type of the override importer.  
[GetImporterType](AssetDatabase.GetImporterType.html)| Returns the type of
importer associated with an asset without loading the asset.  
[GetImporterTypes](AssetDatabase.GetImporterTypes.html)| Returns the types of
importers associated with the specified array of assets, without loading those
assets.  
[GetLabels](AssetDatabase.GetLabels.html)| Returns all labels attached to a
given asset.  
[GetMainAssetTypeAtPath](AssetDatabase.GetMainAssetTypeAtPath.html)| Returns
the type of the main asset object at assetPath.  
[GetMainAssetTypeFromGUID](AssetDatabase.GetMainAssetTypeFromGUID.html)|
Returns the type of the main asset object with guid.  
[GetScriptableObjectsWithMissingScriptCount](AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html)|
Checks how many unloadable ScriptableObject instances are present in the
specified asset.  
[GetSubFolders](AssetDatabase.GetSubFolders.html)| Given a path to a directory
in the Assets folder, relative to the project folder, this method will return
an array of all its subdirectories.  
[GetTextMetaFilePathFromAssetPath](AssetDatabase.GetTextMetaFilePathFromAssetPath.html)|
Gets the path to the text .meta file associated with an asset.  
[GetTypeFromPathAndFileID](AssetDatabase.GetTypeFromPathAndFileID.html)| Gets
an object's type from an Asset path and a local file identifier.  
[GetUnusedAssetBundleNames](AssetDatabase.GetUnusedAssetBundleNames.html)|
Return all the unused assetBundle names in the asset database.  
[GUIDFromAssetPath](AssetDatabase.GUIDFromAssetPath.html)| Get the GUID for
the asset at path.  
[GUIDToAssetPath](AssetDatabase.GUIDToAssetPath.html)| Gets the corresponding
asset path for the supplied GUID, or an empty string if the GUID can't be
found.  
[ImportAsset](AssetDatabase.ImportAsset.html)| Import asset at path.  
[ImportPackage](AssetDatabase.ImportPackage.html)| Imports package at
packagePath into the current project.  
[InstanceIDsToGUIDs](AssetDatabase.InstanceIDsToGUIDs.html)| Sets a
NativeArray of UnityEditor.GUIDs for every valid Instance ID that is an asset.  
[IsCacheServerEnabled](AssetDatabase.IsCacheServerEnabled.html)| Checks
whether the Cache Server is enabled in Project Settings.  
[IsConnectedToCacheServer](AssetDatabase.IsConnectedToCacheServer.html)|
Checks connection status of the Cache Server.  
[IsDirectoryMonitoringEnabled](AssetDatabase.IsDirectoryMonitoringEnabled.html)|
Reports whether Directory Monitoring is enabled.  
[IsForeignAsset](AssetDatabase.IsForeignAsset.html)| Determines whether the
Asset is a foreign Asset.  
[IsMainAsset](AssetDatabase.IsMainAsset.html)| Is asset a main asset in the
project window?  
[IsMainAssetAtPathLoaded](AssetDatabase.IsMainAssetAtPathLoaded.html)| Returns
true if the main asset object at assetPath is loaded in memory.  
[IsMetaFileOpenForEdit](AssetDatabase.IsMetaFileOpenForEdit.html)| Query
whether an asset's metadata (.meta) file is open for edit in version control.  
[IsNativeAsset](AssetDatabase.IsNativeAsset.html)| Determines whether the
Asset is a native Asset.  
[IsOpenForEdit](AssetDatabase.IsOpenForEdit.html)| Query whether an Asset file
is open for editing in version control.  
[IsSubAsset](AssetDatabase.IsSubAsset.html)| Does the asset form part of
another asset?  
[IsValidFolder](AssetDatabase.IsValidFolder.html)| Given a path to a folder,
returns true if it exists, false otherwise.  
[LoadAllAssetRepresentationsAtPath](AssetDatabase.LoadAllAssetRepresentationsAtPath.html)|
Returns all sub Assets at assetPath.  
[LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)| Returns an
array of all Assets at assetPath.  
[LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)| Returns the first asset
object of type type at given path assetPath.  
[LoadMainAssetAtPath](AssetDatabase.LoadMainAssetAtPath.html)| Returns the
main asset object at assetPath.The "main" Asset is the Asset at the root of a
hierarchy (such as a Maya file which may contain multiples meshes and
GameObjects).  
[LoadObjectAsync](AssetDatabase.LoadObjectAsync.html)| Loads a specific Object
and its dependencies from an Asset file asynchronously.  
[MakeEditable](AssetDatabase.MakeEditable.html)| Makes a file open for editing
in version control.  
[MoveAsset](AssetDatabase.MoveAsset.html)| Move an asset file (or folder) from
one folder to another.  
[MoveAssetsToTrash](AssetDatabase.MoveAssetsToTrash.html)| Lets you move
multiple assets or folders to trash at once with performance benefits under
version control.  
[MoveAssetToTrash](AssetDatabase.MoveAssetToTrash.html)| Moves the specified
asset or folder to the OS trash.  
[OpenAsset](AssetDatabase.OpenAsset.html)| Opens the asset with associated
application.  
[Refresh](AssetDatabase.Refresh.html)| Import any changed assets.  
[RefreshSettings](AssetDatabase.RefreshSettings.html)| Apply pending Editor
Settings changes to the Asset pipeline.  
[RegisterCustomDependency](AssetDatabase.RegisterCustomDependency.html)|
Allows you to register a custom dependency that Assets can be dependent on. If
you register a custom dependency, and specify that an Asset is dependent on
it, then the Asset will get re-imported if the custom dependency changes.  
[ReleaseCachedFileHandles](AssetDatabase.ReleaseCachedFileHandles.html)|
Calling this function will release file handles internally cached by Unity.
This allows modifying asset or meta files safely thus avoiding potential file
sharing IO errors.  
[RemoveAssetBundleName](AssetDatabase.RemoveAssetBundleName.html)| Remove the
assetBundle name from the asset database. The forceRemove flag is used to
indicate if you want to remove it even it's in use.  
[RemoveObjectFromAsset](AssetDatabase.RemoveObjectFromAsset.html)| Removes
object from its asset (Additional resources: AssetDatabase.AddObjectToAsset).  
[RemoveScriptableObjectsWithMissingScript](AssetDatabase.RemoveScriptableObjectsWithMissingScript.html)|
Removes any ScriptableObject instances from the given asset file which cannot
be loaded because their scripts could not be found.  
[RemoveUnusedAssetBundleNames](AssetDatabase.RemoveUnusedAssetBundleNames.html)|
Remove all the unused assetBundle names in the asset database.  
[RenameAsset](AssetDatabase.RenameAsset.html)| Rename an asset file.  
[ResetCacheServerReconnectTimer](AssetDatabase.ResetCacheServerReconnectTimer.html)|
Resets the internal cache server connection reconnect timer values. The
default delay timer value is 1 second, and the max delay value is 5 minutes.
Everytime a connection attempt fails it will double the delay timer value,
until a maximum time of the max value.  
[SaveAssetIfDirty](AssetDatabase.SaveAssetIfDirty.html)| Writes all unsaved
changes to the specified asset to disk.  
[SaveAssets](AssetDatabase.SaveAssets.html)| Writes all unsaved asset changes
to disk.  
[SetImporterOverride](AssetDatabase.SetImporterOverride.html)| Sets a specific
importer to use for the asset.  
[SetLabels](AssetDatabase.SetLabels.html)| Replaces that list of labels on an
asset.  
[SetMainObject](AssetDatabase.SetMainObject.html)| Specifies which object in
the asset file should become the main object after the next import.  
[StartAssetEditing](AssetDatabase.StartAssetEditing.html)| Places the Asset
Database into a state that temporarily prevents automatic import, allowing you
to group several asset imports together into one larger import.  
[StopAssetEditing](AssetDatabase.StopAssetEditing.html)| Ends the Asset
Database's temporary paused state, allowing it to resume normal automatic
imports.  
[TryGetAssetFolderInfo](AssetDatabase.TryGetAssetFolderInfo.html)| Get
AssetDatabase specific information about a folder.  
[TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)|
Get the GUID and local file id from an object instance id.  
[UnregisterCustomDependencyPrefixFilter](AssetDatabase.UnregisterCustomDependencyPrefixFilter.html)|
Removes custom dependencies that match the prefixFilter.  
[ValidateMoveAsset](AssetDatabase.ValidateMoveAsset.html)| Checks if an asset
file can be moved from one folder to another. (Without actually moving the
file).  
[WriteImportSettingsIfDirty](AssetDatabase.WriteImportSettingsIfDirty.html)|
Writes the import settings to disk.  
  
### Events

[cacheServerConnectionChanged](AssetDatabase-
cacheServerConnectionChanged.html)| Unity raises this event when Cache Server
connection is changed.  
---|---  
[importPackageCancelled](AssetDatabase-importPackageCancelled.html)| Callback
raised whenever a package import is cancelled by the user.  
[importPackageCompleted](AssetDatabase-importPackageCompleted.html)| Callback
raised whenever a package import successfully completes.  
[importPackageFailed](AssetDatabase-importPackageFailed.html)| Callback raised
whenever a package import failed.  
[importPackageStarted](AssetDatabase-importPackageStarted.html)| Callback
raised whenever a package import starts.  
  
### Delegates

[ImportPackageCallback](AssetDatabase.ImportPackageCallback.html)| Delegate to
be called from AssetDatabase.ImportPackage callbacks. packageName is the name
of the package that raised the callback.  
---|---  
[ImportPackageFailedCallback](AssetDatabase.ImportPackageFailedCallback.html)|
Delegate to be called from AssetDatabase.ImportPackage callbacks. packageName
is the name of the package that raised the callback. errorMessage is the
reason for the failure.  
  
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

