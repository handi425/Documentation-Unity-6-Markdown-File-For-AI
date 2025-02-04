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

**Method group is Obsolete**  

#  [AssemblyBuilder](Compilation.AssemblyBuilder.html).Build

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

**Obsolete** This feature is being deprecated and will be removed in the
future. Similar functionality can be achieved using the Roslyn compiler.

## Declaration

public bool Build();

### Returns

**bool** Returns true if build was started. Returns false if the build was not
started due to the editor currently compiling scripts in the Assets folder.

### Description

Starts the build of the assembly.  
  
While building, the small progress icon in the lower right corner of Unity's
main window will spin and [EditorApplication.isCompiling](EditorApplication-
isCompiling.html) will return true.

Use AssemblyBuilder.buildStarted and AssemblyBuilder.buildFinished to get
notified when the build has started and finished.  
  
Additional resources: AssemblyBuilder.buildStarted,
AssemblyBuilder.buildFinished, AssemblyBuilder.status.

    
    
    using System.IO;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Compilation;
    using UnityEngine;  
      
    public class AssembyBuilderExample
    {
        [[MenuItem](MenuItem.html)("AssemblyBuilder Example/Build [Assembly](Compilation.Assembly.html) Async")]
        public static void BuildAssemblyAsync()
        {
            BuildAssembly(false);
        }  
      
        [[MenuItem](MenuItem.html)("AssemblyBuilder Example/Build [Assembly](Compilation.Assembly.html) Sync")]
        public static void BuildAssemblySync()
        {
            BuildAssembly(true);
        }  
      
        static void BuildAssembly(bool wait)
        {
            var scripts = new[] { "Temp/MyAssembly/MyScript1.cs", "Temp/MyAssembly/MyScript2.cs" };
            var outputAssembly = "Temp/MyAssembly/MyAssembly.dll";
            var assemblyProjectPath = "Assets/MyAssembly.dll";  
      
            [Directory.CreateDirectory](Windows.Directory.CreateDirectory.html)("Temp/MyAssembly");  
      
            // Create scripts
            foreach (var scriptPath in scripts)
            {
                var scriptName = Path.GetFileNameWithoutExtension(scriptPath);
                File.WriteAllText(scriptPath, string.Format("using UnityEngine; public class {0} : [MonoBehaviour](MonoBehaviour.html) {{ void Start() {{ [Debug.Log](Debug.Log.html)(\"{0}\"); }} }}", scriptName));
            }  
      
            var assemblyBuilder = new AssemblyBuilder(outputAssembly, scripts);  
      
            // Exclude a reference to the copy of the assembly in the Assets folder, if any.
            assemblyBuilder.excludeReferences = new string[] { assemblyProjectPath };  
      
            // Called on main thread
            assemblyBuilder.buildStarted += delegate(string assemblyPath)
            {
                [Debug.LogFormat](Debug.LogFormat.html)("[Assembly](Compilation.Assembly.html) build started for {0}", assemblyPath);
            };  
      
            // Called on main thread
            assemblyBuilder.buildFinished += delegate(string assemblyPath, [CompilerMessage](Compilation.CompilerMessage.html)[] compilerMessages)
            {
                var errorCount = compilerMessages.Count(m => m.type == [CompilerMessageType.Error](Compilation.CompilerMessageType.Error.html));
                var warningCount = compilerMessages.Count(m => m.type == [CompilerMessageType.Warning](Compilation.CompilerMessageType.Warning.html));  
      
                [Debug.LogFormat](Debug.LogFormat.html)("[Assembly](Compilation.Assembly.html) build finished for {0}", assemblyPath);
                [Debug.LogFormat](Debug.LogFormat.html)("Warnings: {0} - Errors: {0}", errorCount, warningCount);  
      
                if(errorCount == 0)
                {
                    File.Copy(outputAssembly, assemblyProjectPath, true);
                    [AssetDatabase.ImportAsset](AssetDatabase.ImportAsset.html)(assemblyProjectPath);
                }
            };  
      
            // Start build of assembly
            if(!assemblyBuilder.Build())
            {
                [Debug.LogErrorFormat](Debug.LogErrorFormat.html)("Failed to start build of assembly {0}!", assemblyBuilder.assemblyPath);
                return;
            }  
      
            if(wait)
            {
                while(assemblyBuilder.status != [AssemblyBuilderStatus.Finished](Compilation.AssemblyBuilderStatus.Finished.html))
                    System.Threading.Thread.Sleep(10);
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

