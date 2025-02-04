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

# EditorConnection

class in UnityEditor.Networking.PlayerConnection

/

Inherits from:[ScriptableSingleton_1](ScriptableSingleton_1.html)

Leave feedback

  

Implements
interfaces:[IEditorPlayerConnection](Networking.PlayerConnection.IEditorPlayerConnection.html)

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

Handles the connection from the Editor to the Player.

Sets up events for connecting to and sending data to the Player.  
  
This is a singleton class and can be accessed using EditorConnection.instance.  
  
This can only be used in a class that inherits from MonoBehaviour, Object or
ScriptableObject.  
  
Set the "Autoconnect Profiler" in the Build Settings or build the Player
through code with the BuildPipeline using build options:
[BuildOptions.ConnectToHost](BuildOptions.ConnectToHost.html) and
[BuildOptions.Development](BuildOptions.Development.html) to initialize the
connection.  
  
The Player ID is used to tell multiple connected Players apart. By default,
data is sent to all Players. A connected Player's ID is not guaranteed to be
the same the next time it connects.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Text;
    using UnityEditor.Networking.PlayerConnection;
    using UnityEngine.Networking.PlayerConnection;  
      
    public class EditorConnectionExample : [EditorWindow](EditorWindow.html)
    {
        public static readonly Guid kMsgSendEditorToPlayer = new Guid("EXAMPLEGUID");
        public static readonly Guid kMsgSendPlayerToEditor = new Guid("EXAMPLEGUID");  
      
        [[MenuItem](MenuItem.html)("Test/EditorConnectionExample")]
        static void Init()
        {
            EditorConnectionExample window = (EditorConnectionExample)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(EditorConnectionExample));
            window.Show();
            window.titleContent = new [GUIContent](GUIContent.html)("EditorConnectionExample");
        }  
      
        void OnEnable()
        {
            EditorConnection.instance.Initialize();
            EditorConnection.instance.Register(kMsgSendPlayerToEditor, OnMessageEvent);
        }  
      
        void OnDisable()
        {
            EditorConnection.instance.Unregister(kMsgSendPlayerToEditor, OnMessageEvent);
            EditorConnection.instance.DisconnectAll();
        }  
      
        private void OnMessageEvent([MessageEventArgs](Networking.PlayerConnection.MessageEventArgs.html) args)
        {
            var text = Encoding.ASCII.GetString(args.data);
            [Debug.Log](Debug.Log.html)("[Message](VersionControl.Message.html) from player: " + text);
        }  
      
        void OnGUI()
        {
            var playerCount = EditorConnection.instance.ConnectedPlayers.Count;
            StringBuilder builder = new StringBuilder();
            builder.AppendLine(string.Format("{0} players connected.", playerCount));
            int i = 0;
            foreach (var p in EditorConnection.instance.ConnectedPlayers)
            {
                builder.AppendLine(string.Format("[{0}] - {1} {2}", i++, p.name, p.playerId));
            }
            [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)(builder.ToString(), [MessageType.Info](MessageType.Info.html));  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Send message to player"))
            {
                EditorConnection.instance.Send(kMsgSendEditorToPlayer, Encoding.ASCII.GetBytes("Hello from [Editor](Editor.html)"));
            }
        }
    }
    

### Properties

[ConnectedPlayers](Networking.PlayerConnection.EditorConnection.ConnectedPlayers.html)|
A list of the connected Players.  
---|---  
  
### Public Methods

[DisconnectAll](Networking.PlayerConnection.EditorConnection.DisconnectAll.html)|
Disconnects all of the active connections between the Editor and the Players.  
---|---  
[Initialize](Networking.PlayerConnection.EditorConnection.Initialize.html)|
Initializes the EditorConnection.  
[Register](Networking.PlayerConnection.EditorConnection.Register.html)|
Registers a callback on a certain message ID.  
[RegisterConnection](Networking.PlayerConnection.EditorConnection.RegisterConnection.html)|
Registers a callback, executed when a new Player connects to the Editor.  
[RegisterDisconnection](Networking.PlayerConnection.EditorConnection.RegisterDisconnection.html)|
Registers a callback on a Player when that Player disconnects.  
[Send](Networking.PlayerConnection.EditorConnection.Send.html)| Sends data to
the connected Players.  
[TrySend](Networking.PlayerConnection.EditorConnection.TrySend.html)| Attempts
to send data from the Editor to the connected Players.  
[Unregister](Networking.PlayerConnection.EditorConnection.Unregister.html)|
Deregisters a registered callback.  
[UnregisterConnection](Networking.PlayerConnection.EditorConnection.UnregisterConnection.html)|
Unregisters the connection callback.  
[UnregisterDisconnection](Networking.PlayerConnection.EditorConnection.UnregisterDisconnection.html)|
Unregisters the disconnection callback.  
  
### Inherited Members

### Static Properties

[instance](ScriptableSingleton_1-instance.html)| Gets the instance of the
Singleton. Unity creates the Singleton instance when this property is accessed
for the first time. If you use the FilePathAttribute, then Unity loads the
data on the first access as well.  
---|---  
  
### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[Save](ScriptableSingleton_1.Save.html)| Saves the current state of the
ScriptableSingleton.  
---|---  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
[GetFilePath](ScriptableSingleton_1.GetFilePath.html)| Get the file path where
this ScriptableSingleton is saved to.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

