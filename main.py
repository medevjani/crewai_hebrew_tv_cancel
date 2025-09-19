from tasks.cancellation_flow import run_cancellation_flow

if __name__ == "__main__":
    transcript_file, voice_files = run_cancellation_flow()
    print("Transcript saved to:", transcript_file)
    print("Voice files:", voice_files)
