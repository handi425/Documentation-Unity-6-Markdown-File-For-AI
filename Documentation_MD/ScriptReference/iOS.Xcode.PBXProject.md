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

# PBXProject

class in UnityEditor.iOS.Xcode

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

Represents an Xcode project (pbxproj file).

    
    
    using System.Collections;
    using System.Collections.Generic;
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_PBXProject  
    {
        [PostProcessBuild]
        public static void OnPostprocessBuild([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {
            // Stop processing if build target is not [iOS](PlayerSettings.iOS.html)
            if (buildTarget != [BuildTarget.iOS](BuildTarget.iOS.html))
                return;  
      
            // Initialize [PBXProject](iOS.Xcode.PBXProject.html)
            string projectPath = [PBXProject.GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)(pathToBuiltProject);
            [PBXProject](iOS.Xcode.PBXProject.html) pbxProject = new [PBXProject](iOS.Xcode.PBXProject.html)();
            pbxProject.ReadFromFile(projectPath);  
      
            // Perform any modifications you want to the [PBXProject](iOS.Xcode.PBXProject.html)  
      
            // Get the target GUID
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Add a new build configuration and add a new property to it
            string configName = "exampleConfig";
            pbxProject.AddBuildConfig(configName);
            string configGuid = pbxProject.BuildConfigByName(mainTargetGuid, configName);
            pbxProject.AddBuildPropertyForConfig(configGuid, "exampleProperty", "exampleValue");  
      
            // Add a new file to project and to build list
            string filePath = Path.Combine([Application.dataPath](Application-dataPath.html), "[Resources](Resources.html)/InputFile.txt");
            string fileGuid = pbxProject.AddFile(filePath, "[Resources](Resources.html)/InputFile.txt");
            pbxProject.AddFileToBuild(mainTargetGuid, fileGuid);  
      
            // Add frameworks to the project
            pbxProject.AddFrameworkToProject(mainTargetGuid, "CoreBluetooth.framework", false);
            pbxProject.AddFrameworkToProject(mainTargetGuid, "MapKit.framework", true);  
      
            // Apply changes to the pbxproj file
            pbxProject.WriteToFile(projectPath);
        }  
      
    }
    

### Properties

[unityPostprocessTargetPhonyBuildPhaseName](iOS.Xcode.PBXProject-
unityPostprocessTargetPhonyBuildPhaseName.html)| The name of the placeholder
build phase, which Unity adds to indicate a place to add post-processing
actions.  
---|---  
  
### Constructors

[PBXProject](iOS.Xcode.PBXProject-ctor.html)| Creates a new instance of
PBXProject class.  
---|---  
  
### Public Methods

[AddAssetTagForFile](iOS.Xcode.PBXProject.AddAssetTagForFile.html)| Adds an
asset tag for the given file.  
---|---  
[AddAssetTagToDefaultInstall](iOS.Xcode.PBXProject.AddAssetTagToDefaultInstall.html)|
Adds the asset tag to the list of tags to download during initial
installation.  
[AddBuildConfig](iOS.Xcode.PBXProject.AddBuildConfig.html)| Creates a new set
of build configurations for all targets in the project.  
[AddBuildProperty](iOS.Xcode.PBXProject.AddBuildProperty.html)| Adds a value
to the build property list in all the build configurations for the specified
target(s).  
[AddBuildPropertyForConfig](iOS.Xcode.PBXProject.AddBuildPropertyForConfig.html)|
Adds a value to build property list of the given build configuration(s).  
[AddCapability](iOS.Xcode.PBXProject.AddCapability.html)| Adds a target
capability to the Xcode project.  
[AddCopyFilesBuildPhase](iOS.Xcode.PBXProject.AddCopyFilesBuildPhase.html)|
Creates a new Copy Files build phase for a given target.  
[AddCopyFilesBuildPhaseBeforeTargetPostprocess](iOS.Xcode.PBXProject.AddCopyFilesBuildPhaseBeforeTargetPostprocess.html)|
Creates a new Copy Files build phase for a given target.  
[AddFile](iOS.Xcode.PBXProject.AddFile.html)| Adds a new file reference to the
list of known files.  
[AddFileToBuild](iOS.Xcode.PBXProject.AddFileToBuild.html)| Configure a file
to build for the given native target.  
[AddFileToBuildSection](iOS.Xcode.PBXProject.AddFileToBuildSection.html)|
Configures file for building for the given native target on specific build
section.  
[AddFileToBuildWithFlags](iOS.Xcode.PBXProject.AddFileToBuildWithFlags.html)|
Configure a file for building for the given target with specific compiler
flags.  
[AddFolderReference](iOS.Xcode.PBXProject.AddFolderReference.html)| Adds a new
folder reference to the list of known files.  
[AddFrameworksBuildPhase](iOS.Xcode.PBXProject.AddFrameworksBuildPhase.html)|
Creates a new frameworks build phase for given target.  
[AddFrameworkToProject](iOS.Xcode.PBXProject.AddFrameworkToProject.html)| Adds
a system framework dependency for the specified target.  
[AddHeadersBuildPhase](iOS.Xcode.PBXProject.AddHeadersBuildPhase.html)|
Creates a new headers build phase for a given target.  
[AddKnownRegion](iOS.Xcode.PBXProject.AddKnownRegion.html)| Adds the provided
regions to the Xcode Project.  
[AddLocaleVariantFile](iOS.Xcode.PBXProject.AddLocaleVariantFile.html)| Adds
Locale to Variant Group of Xcode Project for iOS platform.  
[AddPublicHeaderToBuild](iOS.Xcode.PBXProject.AddPublicHeaderToBuild.html)|
Configures a file for building for the given native target as a public header.  
[AddRemotePackageFrameworkToProject](iOS.Xcode.PBXProject.AddRemotePackageFrameworkToProject.html)|
Adds a remote package framework dependency for the specified target.  
[AddRemotePackageReferenceAtBranch](iOS.Xcode.PBXProject.AddRemotePackageReferenceAtBranch.html)|
Adds a reference to the remote package at the given branch.  
[AddRemotePackageReferenceAtRevision](iOS.Xcode.PBXProject.AddRemotePackageReferenceAtRevision.html)|
Adds a reference to the remote package at the given revision.  
[AddRemotePackageReferenceAtVersion](iOS.Xcode.PBXProject.AddRemotePackageReferenceAtVersion.html)|
Adds a reference to the remote package at the given version.  
[AddRemotePackageReferenceAtVersionUpToNextMajor](iOS.Xcode.PBXProject.AddRemotePackageReferenceAtVersionUpToNextMajor.html)|
Adds a reference to the remote package at the given version and allows updates
up to the next major version.  
[AddRemotePackageReferenceAtVersionUpToNextMinor](iOS.Xcode.PBXProject.AddRemotePackageReferenceAtVersionUpToNextMinor.html)|
Adds a reference to the remote package at the given version and allows updates
up to the next minor version.  
[AddRemotePackageReferenceWithVersionRange](iOS.Xcode.PBXProject.AddRemotePackageReferenceWithVersionRange.html)|
Adds a reference to the remote package and allows updates in the given version
range.  
[AddResourcesBuildPhase](iOS.Xcode.PBXProject.AddResourcesBuildPhase.html)|
Creates a new resources build phase for a given target.  
[AddShellScriptBuildPhase](iOS.Xcode.PBXProject.AddShellScriptBuildPhase.html)|
Creates a new copy shell script phase for a given target.  
[AddShellScriptBuildPhaseBeforeTargetPostprocess](iOS.Xcode.PBXProject.AddShellScriptBuildPhaseBeforeTargetPostprocess.html)|
Creates a new copy shell script phase for a given target.  
[AddSourcesBuildPhase](iOS.Xcode.PBXProject.AddSourcesBuildPhase.html)|
Creates a new sources build phase for a given target.  
[AddTarget](iOS.Xcode.PBXProject.AddTarget.html)| Creates a new native target.  
[AddTargetDependency](iOS.Xcode.PBXProject.AddTargetDependency.html)| Creates
a dependency between this target and another target. The other target may be
in a different project.  
[BuildConfigByName](iOS.Xcode.PBXProject.BuildConfigByName.html)| Returns the
GUID of build configuration with the given name for the specific target.  
[BuildConfigNames](iOS.Xcode.PBXProject.BuildConfigNames.html)| Returns the
names of the build configurations available in the project.  
[ClearKnownRegions](iOS.Xcode.PBXProject.ClearKnownRegions.html)| Removes the
deprecated regions that get added automatically in Xcode Project.  
[ContainsFileByProjectPath](iOS.Xcode.PBXProject.ContainsFileByProjectPath.html)|
Checks if the project contains a file with the given project path.  
[ContainsFileByRealPath](iOS.Xcode.PBXProject.ContainsFileByRealPath.html)|
Checks if the project contains a file with the given physical path.  
[ContainsFramework](iOS.Xcode.PBXProject.ContainsFramework.html)| Checks
whether the given system framework is a dependency of a target.  
[FindFileGuidByProjectPath](iOS.Xcode.PBXProject.FindFileGuidByProjectPath.html)|
Finds a file with the given project path in the project.  
[FindFileGuidByRealPath](iOS.Xcode.PBXProject.FindFileGuidByRealPath.html)|
Finds a file with the given physical path in the project.  
[GetAllBuildPhasesForTarget](iOS.Xcode.PBXProject.GetAllBuildPhasesForTarget.html)|
Returns all build phases for the specified target.  
[GetBaseReferenceForConfig](iOS.Xcode.PBXProject.GetBaseReferenceForConfig.html)|
Gets the base configuration reference GUID for the specified build
configuration.  
[GetBuildPhaseName](iOS.Xcode.PBXProject.GetBuildPhaseName.html)| Returns the
name of the build phase with the specified GUID.  
[GetBuildPhaseType](iOS.Xcode.PBXProject.GetBuildPhaseType.html)| Returns the
type of the build phase with the specified GUID.  
[GetBuildPropertyForAnyConfig](iOS.Xcode.PBXProject.GetBuildPropertyForAnyConfig.html)|
Gets a build property value for the given name in all the build configurations
for the specified target(s). If a property has multiple values, those are
delimited by a space.  
[GetBuildPropertyForConfig](iOS.Xcode.PBXProject.GetBuildPropertyForConfig.html)|
Gets a build property value for the given name in the specified build
configuration(s). If a property has multiple values they are delimited by a
space.  
[GetCompileFlagsForFile](iOS.Xcode.PBXProject.GetCompileFlagsForFile.html)|
Returns compile flags set for the specific file on a given target.  
[GetCopyFilesBuildPhaseByTarget](iOS.Xcode.PBXProject.GetCopyFilesBuildPhaseByTarget.html)|
Returns the GUID of matching copy files build phase for the given target.  
[GetEntitlementFilePathForTarget](iOS.Xcode.PBXProject.GetEntitlementFilePathForTarget.html)|
Returns the relative path to the entitlement file for the specified build
target.  
[GetFrameworksBuildPhaseByTarget](iOS.Xcode.PBXProject.GetFrameworksBuildPhaseByTarget.html)|
Returns the GUID of frameworks build phase for the given target.  
[GetHeadersBuildPhaseByTarget](iOS.Xcode.PBXProject.GetHeadersBuildPhaseByTarget.html)|
Returns the GUID of the headers build phase for the given target.  
[GetRealPathsOfAllFiles](iOS.Xcode.PBXProject.GetRealPathsOfAllFiles.html)|
Return a list of all known files.  
[GetResourcesBuildPhaseByTarget](iOS.Xcode.PBXProject.GetResourcesBuildPhaseByTarget.html)|
Returns the GUID of resources build phase for the given target.  
[GetShellScriptBuildPhaseForTarget](iOS.Xcode.PBXProject.GetShellScriptBuildPhaseForTarget.html)|
Returns the GUID of matching copy shell script build phase for the given
target.  
[GetSourcesBuildPhaseByTarget](iOS.Xcode.PBXProject.GetSourcesBuildPhaseByTarget.html)|
Returns the GUID of sources build phase for the given target.  
[GetTargetProductFileRef](iOS.Xcode.PBXProject.GetTargetProductFileRef.html)|
Returns the file reference of the artifact created by building target.  
[GetUnityFrameworkTargetGuid](iOS.Xcode.PBXProject.GetUnityFrameworkTargetGuid.html)|
Returns the GUID of the framework target in Unity project.  
[GetUnityMainTargetGuid](iOS.Xcode.PBXProject.GetUnityMainTargetGuid.html)|
Returns the GUID of the main target in Unity project.  
[InsertCopyFilesBuildPhase](iOS.Xcode.PBXProject.InsertCopyFilesBuildPhase.html)|
Creates a new copy files build phase for a given target.  
[InsertShellScriptBuildPhase](iOS.Xcode.PBXProject.InsertShellScriptBuildPhase.html)|
Creates a new shell script build phase for a given target.  
[ProjectGuid](iOS.Xcode.PBXProject.ProjectGuid.html)| Returns the GUID of the
project.  
[ReadFromFile](iOS.Xcode.PBXProject.ReadFromFile.html)| Reads the project from
a file identified by the given path.  
[ReadFromStream](iOS.Xcode.PBXProject.ReadFromStream.html)| Reads the project
from the given text reader.  
[ReadFromString](iOS.Xcode.PBXProject.ReadFromString.html)| Reads the project
from the given string.  
[RemoveAssetTag](iOS.Xcode.PBXProject.RemoveAssetTag.html)| Removes an asset
tag.  
[RemoveAssetTagForFile](iOS.Xcode.PBXProject.RemoveAssetTagForFile.html)|
Removes an asset tag for the given file.  
[RemoveAssetTagFromDefaultInstall](iOS.Xcode.PBXProject.RemoveAssetTagFromDefaultInstall.html)|
Removes the asset tag from the list of tags to download during initial
installation.  
[RemoveBuildConfig](iOS.Xcode.PBXProject.RemoveBuildConfig.html)| Removes all
build configurations with the given name from all targets in the project.  
[RemoveFile](iOS.Xcode.PBXProject.RemoveFile.html)| Removes the given file
from project.  
[RemoveFileFromBuild](iOS.Xcode.PBXProject.RemoveFileFromBuild.html)| Removes
the given file from the list of files to build for the given target.  
[RemoveFrameworkFromProject](iOS.Xcode.PBXProject.RemoveFrameworkFromProject.html)|
Removes a system framework dependency for the specified target.  
[ReplaceFile](iOS.Xcode.PBXProject.ReplaceFile.html)| Replaces a specified
file with a new file.  
[SetBaseReferenceForConfig](iOS.Xcode.PBXProject.SetBaseReferenceForConfig.html)|
Sets the base configuration reference for the specified build configuration.  
[SetBuildProperty](iOS.Xcode.PBXProject.SetBuildProperty.html)| Sets a build
property to the given value in all build configurations for the specified
target(s).  
[SetBuildPropertyForConfig](iOS.Xcode.PBXProject.SetBuildPropertyForConfig.html)|
Sets a build property to the given value in the specified build
configuration(s).  
[SetCompileFlagsForFile](iOS.Xcode.PBXProject.SetCompileFlagsForFile.html)|
Sets the compilation flags for the given file in the given target.  
[SetDevelopmentRegion](iOS.Xcode.PBXProject.SetDevelopmentRegion.html)| Sets
the default language and region for the bundle in Xcode Project.  
[SetTeamId](iOS.Xcode.PBXProject.SetTeamId.html)| Sets the Team ID of an Xcode
project.  
[TargetGuidByName](iOS.Xcode.PBXProject.TargetGuidByName.html)| Returns the
GUID of the native target with the given name.  
[UpdateBuildProperty](iOS.Xcode.PBXProject.UpdateBuildProperty.html)| Adds and
removes values from a build property in all build configurations for the
specified target(s).  
[UpdateBuildPropertyForConfig](iOS.Xcode.PBXProject.UpdateBuildPropertyForConfig.html)|
Adds and removes values from a build property in the given build
configuration.  
[WriteToFile](iOS.Xcode.PBXProject.WriteToFile.html)| Writes the project
contents to the specified file.  
[WriteToStream](iOS.Xcode.PBXProject.WriteToStream.html)| Writes the project
contents to the specified text writer.  
[WriteToString](iOS.Xcode.PBXProject.WriteToString.html)| Writes the contents
of the project to string.  
  
### Static Methods

[GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)| Returns the
path to PBX project in the given Unity build path.  
---|---  
[GetUnityTestTargetName](iOS.Xcode.PBXProject.GetUnityTestTargetName.html)|
Returns the default test target name.  
[IsBuildable](iOS.Xcode.PBXProject.IsBuildable.html)| Checks if a file with
the given extension can be built by Xcode.  
[IsKnownExtension](iOS.Xcode.PBXProject.IsKnownExtension.html)| Checks if
files with the given extension are known to PBXProject.  
  
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

